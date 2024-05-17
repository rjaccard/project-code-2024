"""
Usage:
    flan_sft.py [options] --out=File --cfg=FILE --data=FILE [--dev_mode=BOOL]

Options:
    -h --help     Show this help message.
    --version     Show the version.
    --out=File  Output file path.
    --dev_mode=BOOL Development mode.
    --cfg=FILE  Config file path.
    --data=FILE  Data file path.
"""

import docopt
import nltk
import yaml
import wandb
import json
import os
from datasets import load_dataset, load_from_disk, DatasetDict, concatenate_datasets
from transformers import T5Tokenizer, DataCollatorForSeq2Seq
from transformers import (
    T5ForConditionalGeneration,
    Seq2SeqTrainingArguments,
    Seq2SeqTrainer,
)

nltk.download("punkt", quiet=True)


def print_number_of_trainable_model_parameters(model):
    trainable_model_params = 0
    all_model_params = 0
    for _, param in model.named_parameters():
        all_model_params += param.numel()
        if param.requires_grad:
            trainable_model_params += param.numel()
    return f"trainable model parameters: {trainable_model_params}\nall model parameters: {all_model_params}\npercentage of trainable model parameters: {100 * trainable_model_params / all_model_params:.2f}%"


def tokenize_dataset(examples, tokenizer):
    model_inputs = tokenizer(examples["question"], max_length=512, truncation=True)
    labels = tokenizer(examples["answer"], max_length=512, truncation=True)
    model_inputs["labels"] = labels["input_ids"]
    return model_inputs


def process_metamathqa(examples, prefix="Please answer the following question: "):
    """Add a prefix to the inputs and tokenize the inputs and targets.

    Args:
        examples: dataset examples.
        tokenizer: tokenizer.
        prefix (str, optional): Prefix to add to each inputs. Defaults to "Please answer the following question: ".

    Returns:
        dataset: processed examples.
    """
    # The "inputs" are the tokenized answer:
    inputs = [prefix + doc for doc in examples["query"]]

    labels = examples["response"]
    return {"question": inputs, "answer": labels}


def load_metamathqa(dev_mode=False):
    """Load the metamathqa dataset.

    Returns:
        Dataset: metamathqa dataset.
    """
    dataset = load_dataset("meta-math/MetaMathQA")
    if dev_mode:
        dataset["train"] = dataset["train"].select(range(20))  # For development
    else:
        dataset["train"] = dataset["train"].select(range(50000))  # For fine-tuning
    dataset = dataset["train"].train_test_split(test_size=0.2)
    tokenized_dataset = dataset.map(
        process_metamathqa,
        batched=True,
        remove_columns=["query", "response", "type", "original_question"],
    )
    return tokenized_dataset


def prepare_dataset(tokenizer, data_path, dev_mode=False):
    """Prepare the dataset.

    Args:
        cfg (dict): configuration.
        tokenizer: tokenizer.
        dev_mode (bool, optional): development mode. Defaults to False.

    Returns:
        Dataset: processed dataset.
    """
    dataset_class = load_from_disk(data_path)
    metamath_qa = load_metamathqa(dev_mode)
    dataset = DatasetDict()
    dataset["train"] = concatenate_datasets(
        [dataset_class["train"], metamath_qa["train"]]
    ).shuffle(seed=42)
    dataset["test"] = concatenate_datasets(
        [dataset_class["test"], metamath_qa["test"]]
    ).shuffle(seed=42)

    dataset = dataset.map(
        lambda examples: tokenize_dataset(examples, tokenizer),
        batched=True,
        remove_columns=["question", "answer"],
    )
    return dataset


def finetune(cfg, output, data_path, dev_mode=False) -> None:
    """Full Finetuning of the model.

    Args:
        cfg (dict): configuration.
        output (str): output path.
        dev_mode (bool, optional): development mode. Defaults to False.
    """
    # Load the model
    print("\n Loading the model...")
    model = T5ForConditionalGeneration.from_pretrained(
        cfg["model"]["model_name"], force_download=True
    )
    tokenizer = T5Tokenizer.from_pretrained(
        cfg["model"]["model_name"], legacy=True, force_download=True
    )
    data_collator = DataCollatorForSeq2Seq(tokenizer=tokenizer, model=model)
    print(print_number_of_trainable_model_parameters(model))
    print("Configuration: \n", json.dumps(cfg, indent=4))

    # Load the dataset
    print("\n Loading and processing the dataset...")
    tokenized_dataset = prepare_dataset(tokenizer, data_path, dev_mode)

    # Training arguments
    training_args = Seq2SeqTrainingArguments(
        output_dir=output,
        evaluation_strategy="epoch",
        save_strategy="epoch",
        learning_rate=cfg["model"]["learning_rate"],
        lr_scheduler_type="cosine",
        weight_decay=cfg["model"]["weight_decay"],
        num_train_epochs=cfg["model"]["num_epochs"],
        predict_with_generate=True,
        auto_find_batch_size=True,
        load_best_model_at_end=True,
        save_total_limit=1,
        report_to="wandb",
        run_name="flan-t5-full-finetuning",
    )

    # Trainer
    trainer = Seq2SeqTrainer(
        model=model,
        data_collator=data_collator,
        tokenizer=tokenizer,
        args=training_args,
        train_dataset=tokenized_dataset["train"],
        eval_dataset=tokenized_dataset["test"],
    )

    # Train the model
    print("\n Training the model...")
    trainer.train()
    trainer.save_model(output + "/full_model")


if __name__ == "__main__":
    args = docopt.docopt(__doc__, version="0.1")
    cfg = yaml.safe_load(open(args["--cfg"], "r"))
    data_path = args["--data"]

    if args["--dev_mode"] is not None:
        cfg["model"]["model_name"] = cfg["model"]["model_name_dev"]
        dev_mode = True
    else:
        dev_mode = False

    os.environ["WANDB_PROJECT"] = cfg["wandb"]["project_name"]
    os.environ["WANDB_LOG_MODEL"] = "false"
    wandb.login(key="e4b58cb87bd9b8759692a403f616aa07bbbc85fb")

    finetune(cfg, args["--out"], data_path, dev_mode)
