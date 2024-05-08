import json
import evaluate
import numpy as np

def load_json(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data


def main():
    # Load JSON file
    file_path = '../datasets/small_test_with_ans.json'
    data = load_json(file_path)

    # Extract references and translations
    refs = [entry['query'] for entry in data]
    mt = [entry['answer_T5'] for entry in data]

    # Compute scores
    bleu = evaluate.load("bleu")
    bert = evaluate.load("bertscore")
    rouge = evaluate.load('rouge')
    meteor = evaluate.load('meteor')

    bleu_score = bleu.compute(predictions=mt, references=refs)
    rouge_score = rouge.compute(predictions=mt, references=refs)
    print(rouge_score)
    bert_score = bert.compute(predictions=mt, references=refs, lang="en")
    print(bert_score)
    meteor_score = meteor.compute(predictions=mt, references=refs)
    print(meteor_score)




    print(bleu_score)

    # Print scores
    print("BLEU Score:", bleu_score['bleu'])
    print("ROUGE-L Score:", rouge_score['rougeL'])
    print("BERTScore:", np.mean(bert_score['f1']))
    print("METEOR Score:", meteor_score['meteor'])


if __name__ == "__main__":
    main()