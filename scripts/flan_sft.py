"""
Usage:
    flan_sft.py [options] --out=File  --cfg=FILE [--dev_mode=BOOL] [--with_lora=BOOL]

Options:
    -h --help     Show this help message.
    --version     Show the version.
    --out=File  Output file path.
    --dev_mode=BOOL Development mode.
    --cfg=FILE  Config file path.
    --with_lora=BOOL  Lora.
"""

import docopt
import nltk
import yaml
import wandb
import os
from datasets import load_dataset
from transformers import T5Tokenizer, DataCollatorForSeq2Seq
from transformers import (
    T5ForConditionalGeneration,
    Seq2SeqTrainingArguments,
    Seq2SeqTrainer,
)
from peft import LoraConfig, get_peft_model, TaskType

nltk.download("punkt", quiet=True)


def print_number_of_trainable_model_parameters(model):
    trainable_model_params = 0
    all_model_params = 0
    for _, param in model.named_parameters():
        all_model_params += param.numel()
        if param.requires_grad:
            trainable_model_params += param.numel()
    return f"trainable model parameters: {trainable_model_params}\nall model parameters: {all_model_params}\npercentage of trainable model parameters: {100 * trainable_model_params / all_model_params:.2f}%"


def preprocess_function(examples, tokenizer, prefix="Please answer the question: "):
    """Add a prefix to the inputs and tokenize the inputs and targets.

    Args:
        examples: dataset examples.
        tokenizer: tokenizer.
        prefix (str, optional): Prefix to add to each inputs. Defaults to "Please answer the question: ".

    Returns:
        dataset: processed examples.
    """
    # The "inputs" are the tokenized answer:
    inputs = [prefix + doc for doc in examples["query"]]
    model_inputs = tokenizer(inputs, max_length=512, truncation=True)

    # The "labels" are the tokenized outputs:
    labels = tokenizer(
        text_target=examples["response"], max_length=512, truncation=True
    )

    model_inputs["labels"] = labels["input_ids"]
    return model_inputs


def prepare_dataset(cfg, tokenizer, dev_mode=False):
    """Load and preprocess the dataset.

    Args:
        cfg (dict): configuration.
        tokenizer: tokenizer.
        dev_mode (bool, optional): development mode. Defaults to False.

    Returns:
        Dataset: tokenized dataset.
    """
    dataset = load_dataset(cfg["data"]["dataset_name"])
    if dev_mode:
        dataset["train"] = dataset["train"].select(range(20))  # For development
    else:
        dataset["train"] = dataset["train"].select(range(50000))  # For fine-tuning
    dataset = dataset["train"].train_test_split(test_size=0.2)
    tokenized_dataset = dataset.map(
        preprocess_function,
        batched=True,
        remove_columns=["query", "response", "type", "original_question"],
        fn_kwargs={"tokenizer": tokenizer},
    )
    return tokenized_dataset


def full_finetune(cfg, output, dev_mode=False) -> None:
    """Full Finetuning of the model.

    Args:
        cfg (dict): configuration.
        output (str): output path.
        dev_mode (bool, optional): development mode. Defaults to False.
    """
    # Load the model
    print("\n Loading the model...")
    model = T5ForConditionalGeneration.from_pretrained(cfg["model"]["model_name"])
    tokenizer = T5Tokenizer.from_pretrained(cfg["model"]["model_name"], legacy=True)
    data_collator = DataCollatorForSeq2Seq(tokenizer=tokenizer, model=model)
    print(print_number_of_trainable_model_parameters(model))

    # Load the dataset
    print("\n Loading and processing the dataset...")
    tokenized_dataset = prepare_dataset(cfg, tokenizer, dev_mode)

    # Training arguments
    training_args = Seq2SeqTrainingArguments(
        output_dir=output,
        evaluation_strategy="epoch",
        save_strategy="epoch",
        learning_rate=cfg["model"]["learning_rate"],
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


def lora_finetune(cfg, output, dev_mode=False) -> None:
    """LoRA Finetuning of the model.

    Args:
        cfg (dict): configuration.
        output (str): output path.
        dev_mode (bool, optional): development mode. Defaults to False.
    """
    # TODO: Implement LORA finetuning
    print("\n Loading the model...")
    model = T5ForConditionalGeneration.from_pretrained(cfg["model"]["model_name"])
    tokenizer = T5Tokenizer.from_pretrained(cfg["model"]["model_name"], legacy=True)
    data_collator = DataCollatorForSeq2Seq(tokenizer=tokenizer, model=model)

    lora_config = LoraConfig(
        r=cfg["model"]["peft"]["rank"],  # Rank
        lora_alpha=cfg["model"]["peft"]["lora_alpha"],
        target_modules=["q", "v"],
        lora_dropout=cfg["model"]["peft"]["lora_dropout"],
        bias="none",
        task_type=TaskType.SEQ_2_SEQ_LM,  # FLAN-T5
    )
    peft_model = get_peft_model(model, lora_config)
    print(print_number_of_trainable_model_parameters(peft_model))

    print("\n Loading and processing the dataset...")
    tokenized_datasets = prepare_dataset(cfg, tokenizer, dev_mode)

    print("\n Training the model...")
    peft_training_args = Seq2SeqTrainingArguments(
        output_dir=output,
        evaluation_strategy="epoch",
        save_strategy="epoch",
        learning_rate=cfg["model"]["peft"]["learning_rate"],
        num_train_epochs=cfg["model"]["peft"]["num_epochs"],
        save_total_limit=1,
        load_best_model_at_end=True,
        auto_find_batch_size=True,
        predict_with_generate=True,
        report_to="wandb",
        run_name="flan-t5-peft-finetuning",
    )

    peft_trainer = Seq2SeqTrainer(
        model=peft_model,
        args=peft_training_args,
        train_dataset=tokenized_datasets["train"],
        eval_dataset=tokenized_datasets["test"],
        data_collator=data_collator,
        tokenizer=tokenizer,
    )

    peft_trainer.train()
    peft_trainer.save_model(output + "/peft_model")


if __name__ == "__main__":
    args = docopt.docopt(__doc__, version="0.1")
    cfg = yaml.safe_load(open(args["--cfg"], "r"))

    if args["--dev_mode"] is not None:
        cfg["model"]["model_name"] = cfg["model"]["model_name_dev"]
        dev_mode = True
    else:
        dev_mode = False

    os.environ["WANDB_PROJECT"] = cfg["wandb"]["project_name"]
    os.environ["WANDB_LOG_MODEL"] = "false"
    wandb.login(key="e4b58cb87bd9b8759692a403f616aa07bbbc85fb")

    print("Configuration: \n", cfg)
    if args["--with_lora"] is not None:
        lora_finetune(cfg, args["--out"], dev_mode)
    else:
        full_finetune(cfg, args["--out"], dev_mode)
