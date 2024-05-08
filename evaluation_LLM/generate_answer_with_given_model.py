import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import json
#from models.model_dpo import AutoDPOModelForSeq2SeqLM

def build_answers():

    # Download the pre-trained model and tokenizer from the Hub
    model_name = "google/flan-t5-small"
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # Initialize your model class and import the pre-trained model into your class
    # Note that if you have a custom module in your class
    # You should initialize the weights of this module in the `__init__` function
    #model_wrapper = AutoDPOModelForSeq2SeqLM(pretrained_model=model)

    max_source_length = 2048
    max_target_length = 512

    # Load your JSON data
    with open('../datasets/small_test_file.json', 'r') as file:
        data = json.load(file)

    # Function to generate answers for questions
    def generate_answers(question):
        input_text = "question: " + question + " answer:"
        inputs = tokenizer(input_text, return_tensors="pt", max_length=max_source_length, truncation=True)

        # Generate model outputs
        with torch.no_grad():
            outputs = model.generate(input_ids=inputs["input_ids"])

        # Decode and return the answer
        return tokenizer.decode(outputs[0], skip_special_tokens=True, max_target_length=max_target_length)

    # Add answers to the JSON data as a new field
    for item in data:
        question = item['query']
        answer = generate_answers(question)
        item['answer_T5'] = answer
        print(answer)

    # Save the modified JSON data back to a file
    with open('../datasets/small_test_with_ans.json', 'w') as file:
        json.dump(data, file)

    print("Answers generated and added to the JSON data.")


if __name__ == "__main__":
    build_answers() 