import torch
from transformers import TrainingArguments, AutoModelForSeq2SeqLM, AutoTokenizer, DataCollatorForSeq2Seq
import yaml
from trl import DPOTrainer
from datasets import load_dataset
import wandb
import os
from peft import LoraConfig, get_peft_model, TaskType

def print_number_of_trainable_model_parameters(model):
    trainable_model_params = 0
    all_model_params = 0
    for _, param in model.named_parameters():
        all_model_params += param.numel()
        if param.requires_grad:
            trainable_model_params += param.numel()
    return f"trainable model parameters: {trainable_model_params}\nall model parameters: {all_model_params}\npercentage of trainable model parameters: {100 * trainable_model_params / all_model_params:.2f}%"


def load_config(config_file):
    with open(config_file, "r") as stream:
        config = yaml.safe_load(stream)
    return config

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
    inputs = [prefix + doc for doc in examples["prompt"]]
    model_inputs = tokenizer(inputs, max_length=512, truncation=True)

    # The "labels" are the tokenized outputs:
    chosen = tokenizer(
        text_target=examples["chosen"], max_length=512, truncation=True
    )
    rejected = tokenizer(
        text_target=examples["rejected"], max_length=512, truncation=True
    )


    model_inputs["chosen"] = chosen["input_ids"]
    model_inputs["rejected"] = chosen["input_ids"]

    return model_inputs

def prepare_dataset(config, tokenizer, dev_mode=False):
    """Load and preprocess the dataset.

    Args:
        cfg (dict): configuration.
        tokenizer: tokenizer.
        dev_mode (bool, optional): development mode. Defaults to False.

    Returns:
        Dataset: tokenized dataset.
    """
    dataset = load_dataset("json", data_files=config["train_dataset"])
    if dev_mode:
        dataset["train"] = dataset["train"].select(range(20))  # For development
    else:
        dataset["train"] = dataset["train"]#.select(range(427))  # For fine-tuning
    dataset = dataset["train"].train_test_split(test_size=0.2)
    #tokenized_dataset = dataset.map(
        #preprocess_function,
        #batched=True,
        #fn_kwargs={"tokenizer": tokenizer},
    #)
    return dataset


def train_model_fft_with_fft(config, device):
    # Load tokenizer and model

    tokenizer = AutoTokenizer.from_pretrained(config['model_name'])
    model = AutoModelForSeq2SeqLM.from_pretrained(config['model_name'])#.to(device)
    print(print_number_of_trainable_model_parameters(model))


    #low_cpu_mem_usage=True,
    #torch_dtype=torch.float16


    dataset = prepare_dataset(config, tokenizer, config['dev_mode'])
    print(dataset)
    # Training arguments
    training_args = TrainingArguments(
        per_device_train_batch_size=config['batch_size'],
        gradient_accumulation_steps=config['batch_size'],
        num_train_epochs=config['num_epochs'],
        output_dir=config['output_dir'],
        overwrite_output_dir=True,
        logging_steps=config['logging_steps'],
        logging_dir=config['logging_dir'],
        save_steps=config['save_steps'],
        report_to="wandb",
        auto_find_batch_size=True,
        #gradient_checkpointing=True,
        learning_rate=2e-5,
        #lr_scheduler_type="cosine",
        #max_steps=max_steps,
        #warmup_steps=max_steps//4,
        )

    # DPO Trainer
    max_prompt_length = 512
    max_length = 1024
    #data_collator = DataCollatorForSeq2Seq(tokenizer=tokenizer, model=model)

    print(dataset['train'])

    print(dataset['test'])
    dpo_trainer = DPOTrainer(
        model=model,
        args=training_args,
        train_dataset=dataset['train'],
        eval_dataset=dataset['test'],
        tokenizer=tokenizer,
        #data_collator=data_collator,
        beta=0.1,
        max_target_length=512,
        max_prompt_length=max_prompt_length,
        max_length=max_length)

    dpo_trainer.train()



def train_model_lora_with_lora(config, device):
    pass
def train_model_lora_with_fft(config, device):
    pass
def train_model_fft_with_lora(config, device):

    # Load tokenizer and model
    print('Loooora')
    tokenizer = AutoTokenizer.from_pretrained(config['model_name'])
    model = AutoModelForSeq2SeqLM.from_pretrained(config['model_name'])#.to(device)

    lora_config = LoraConfig(
        r=64,  # Rank
        lora_alpha=64,
        target_modules=["q", "v"],
        lora_dropout=0.05,
        bias="none",
        task_type=TaskType.SEQ_2_SEQ_LM,  # FLAN-T5
    )
    peft_model = get_peft_model(model, lora_config)
    print(print_number_of_trainable_model_parameters(peft_model))

    #low_cpu_mem_usage=True,
    #torch_dtype=torch.float16


    dataset = prepare_dataset(config, tokenizer, config['dev_mode'])

    # Training arguments
    training_args = TrainingArguments(
        per_device_train_batch_size=config['batch_size'],
        gradient_accumulation_steps=config['batch_size'],
        num_train_epochs=config['num_epochs'],
        evaluation_strategy="steps",
        eval_steps=100,
        save_strategy="steps",
        save_steps=100,
        load_best_model_at_end=True,
        output_dir=config['output_dir'],
        overwrite_output_dir=True,
        logging_steps=config['logging_steps'],
        logging_dir=config['logging_dir'],
        #save_steps=config['save_steps'],
        report_to="wandb",
        auto_find_batch_size=True,
        #gradient_checkpointing=True,
        learning_rate=2e-5,
        #lr_scheduler_type="cosine",
        #max_steps=max_steps,
        #warmup_steps=max_steps//4,
        )

    # DPO Trainer
    max_prompt_length = 512
    max_length = 1024
    #data_collator = DataCollatorForSeq2Seq(tokenizer=tokenizer, model=model)

    print(dataset['train'])

    print(dataset['test'])
    dpo_trainer = DPOTrainer(
        model=peft_model,
        args=training_args,
        train_dataset=dataset['train'],
        eval_dataset=dataset['test'],
        tokenizer=tokenizer,
        #data_collator=data_collator,
        beta=0.1,
        max_target_length=512,
        max_prompt_length=max_prompt_length,
        max_length=max_length)

    dpo_trainer.train()
    dpo_trainer.save_model(config['output_dir'] + "/peft_model")



if __name__ == "__main__":
    config_file = "configs/dpo_config.yaml"
    config = load_config(config_file)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print("Device:", device)

    os.environ["WANDB_PROJECT"] = "DPO"
    os.environ["WANDB_LOG_MODEL"] = "false"
    wandb.login(key="fad71e617dcfeda74b0dd47918dee01c2363a521")

    if config['optimization_type'] == 'lora' and config['model_type'] == 'lora':
        train_model_lora_with_lora(config, device)
    elif config['optimization_type'] == 'lora' and config['model_type'] == 'full_fine_tuning':
        train_model_fft_with_lora(config, device)
    elif config['optimization_type'] == 'full_fine_tuning' and config['model_type'] == 'lora':
        train_model_lora_with_fft(config, device)
    elif config['optimization_type'] == 'full_fine_tuning' and config['model_type'] == 'full_fine_tuning':
        train_model_fft_with_fft(config, device)
    else:
        print("Invalid optimization or model type. Choose either 'lora' or 'full_fine_tuning'.")