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


def train_model_fft_with_fft(config):
    # Load tokenizer and model

    tokenizer = AutoTokenizer.from_pretrained(config['model_path'])
    model = AutoModelForSeq2SeqLM.from_pretrained(config['model_path'])
    print(print_number_of_trainable_model_parameters(model))

    dataset_train = load_dataset("json", data_files=config["train_dataset"])
    dataset_test = load_dataset("json", data_files=config["test_dataset"])

    # Training arguments
    training_args = TrainingArguments(
        #gradient_accumulation_steps=8,

        num_train_epochs=config['num_epochs'],
        evaluation_strategy="epoch",
        eval_steps=config['eval_steps'],
        save_strategy="epoch",
        output_dir=config['output_dir'],
        overwrite_output_dir=True,
        logging_steps=config['logging_steps'],
        report_to="wandb",
        auto_find_batch_size=True,
        learning_rate=config['lr'],
        lr_scheduler_type=config['lr_scheduler'],
        )

    # DPO Trainer
    max_prompt_length = 512
    max_length = 1024

    dpo_trainer = DPOTrainer(
        model=model,
        loss_type='sigmoid',
        args=training_args,
        train_dataset=dataset_train['train'],
        eval_dataset=dataset_test['train'],
        tokenizer=tokenizer,
        beta=config['beta'],
        max_target_length=max_prompt_length,
        max_prompt_length=max_prompt_length,
        max_length=max_length)

    dpo_trainer.train()
    dpo_trainer.save_model(config['output_dir'] + "/full_model")


def train_model_lora_with_lora(config):
    pass
def train_model_lora_with_fft(config):
    pass
def train_model_fft_with_lora(config):

    # Load tokenizer and model
    print('Loooora')
    tokenizer = AutoTokenizer.from_pretrained(config['model_path'])
    model = AutoModelForSeq2SeqLM.from_pretrained(config['model_path'])

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


    dataset_train = load_dataset("json", data_files=config["train_dataset"])
    dataset_test = load_dataset("json", data_files=config["test_dataset"])

    # Training arguments
    training_args = TrainingArguments(
        num_train_epochs=config['num_epochs'],
        evaluation_strategy="epoch",
        eval_steps=config['eval_steps'],
        save_strategy="epoch",
        output_dir=config['output_dir'],
        overwrite_output_dir=True,
        logging_steps=config['logging_steps'],
        report_to="wandb",
        auto_find_batch_size=True,
        learning_rate=config['lr'],
        lr_scheduler_type=config['lr_scheduler'],
        )

    # DPO Trainer
    max_prompt_length = 512
    max_length = 1024


    dpo_trainer = DPOTrainer(
        model=peft_model,
        args=training_args,
        train_dataset=dataset_train['train'],
        eval_dataset=dataset_test['train'],
        tokenizer=tokenizer,
        beta=config['beta'],
        max_target_length=max_prompt_length,
        max_prompt_length=max_prompt_length,
        max_length=max_length)

    dpo_trainer.train()
    dpo_trainer.save_model(config['output_dir'] + "/peft_model")

if __name__ == "__main__":
    config_file = "configs/dpo_config.yaml"
    config = load_config(config_file)

    os.environ["WANDB_PROJECT"] = "DPO"
    os.environ["WANDB_LOG_MODEL"] = "false"
    wandb.login(key="fad71e617dcfeda74b0dd47918dee01c2363a521")

    if config['optimization_type'] == 'lora' and config['model_type'] == 'lora':
        train_model_lora_with_lora(config)
    elif config['optimization_type'] == 'lora' and config['model_type'] == 'full_fine_tuning':
        train_model_fft_with_lora(config)
    elif config['optimization_type'] == 'full_fine_tuning' and config['model_type'] == 'lora':
        train_model_lora_with_fft(config)
    elif config['optimization_type'] == 'full_fine_tuning' and config['model_type'] == 'full_fine_tuning':
        train_model_fft_with_fft(config)
    else:
        print("Invalid optimization or model type. Choose either 'lora' or 'full_fine_tuning'.")