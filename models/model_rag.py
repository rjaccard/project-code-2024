from transformers import (
    AutoConfig, 
    AutoTokenizer, 
    RagConfig, 
    RagTokenizer,
    RagSequenceForGeneration, 
    RagTokenForGeneration,
    RagRetriever
)

import os 
import torch.nn as nn

class RAG(nn.Module):
    def __init__(self, pretrained_model, **kwargs) :

        super().__init__()

        # Retrieve the names or paths of the pre-trained models
        rag_name_or_path = kwargs.get("rag_name_or_path", "facebook/rag-token-nq")
        question_encoder_name_or_path = kwargs.get("question_encoder_name_or_path", "facebook/dpr-question_encoder-single-nq-base")
        generator_name_or_path = kwargs.get("generator_name_or_path", "google/flan-t5-small")
        dataset_path = kwargs.get("dataset_path", "datasets/rag/rag_dataset")
        index_path = kwargs.get("index_path", "datasets/rag/rag_dataset_index.faiss")
        rag_save_dir = kwargs.get("rag_save_dir", "checkpoints/rag_model/")

        # Check if the RAG model is already configured and configure it if not
        if not os.path.exists(pretrained_model) :
            print("RAG model not found. Configuring the model...")
            self.configure_models(rag_name_or_path, question_encoder_name_or_path, generator_name_or_path, rag_save_dir)

        # ====== Load the RAG model ======
        config = RagConfig.from_pretrained(pretrained_model)

        # Set parameters of the retriever
        config.index_name = "custom"
        config.passages_path = dataset_path
        config.index_path = index_path
        config.use_dummy_dataset = False

        # Load the retriever 
        retriever = RagRetriever.from_pretrained(pretrained_model, config=config)
        tokenizer =  RagTokenizer.from_pretrained(pretrained_model)
        model = RagSequenceForGeneration.from_pretrained(pretrained_model, retriever=retriever)

        self.model = model
        self.tokenizer = tokenizer

    def configure_models(self, rag_name_or_path, 
                         question_encoder_name_or_path, 
                         generator_name_or_path, 
                         rag_save_dir = "rag_model/") :

        # Retrieve configurations of the pre-trained models
        rag_config = RagConfig.from_pretrained(rag_name_or_path)
        generator_config = AutoConfig.from_pretrained(generator_name_or_path)
        question_encoder_config = AutoConfig.from_pretrained(question_encoder_name_or_path)
        
        # Set up RAG configuration
        rag_config.generator = generator_config
        rag_config.question_encoder = question_encoder_config
        
        # Set up generator and question encoder 
        rag_model = RagSequenceForGeneration.from_pretrained_question_encoder_generator(
            question_encoder_name_or_path, generator_name_or_path, config=rag_config
        )

        # Load tokenizers for the generator and the question encoder
        generator_tokenizer = AutoTokenizer.from_pretrained(generator_name_or_path)
        question_encoder_tokenizer = AutoTokenizer.from_pretrained(question_encoder_name_or_path)

        # Save the model and the tokenizers
        tokenizer_generator_save_dir = os.path.join(rag_save_dir, "generator_tokenizer")
        tokenizer_question_encoder_save_dir = os.path.join(rag_save_dir, "question_encoder_tokenizer")

        rag_model.save_pretrained(rag_save_dir)
        generator_tokenizer.save_pretrained(tokenizer_generator_save_dir)
        question_encoder_tokenizer.save_pretrained(tokenizer_question_encoder_save_dir)

    def prediction_step(self, input_questions, max_new_tokens=1000) :

        input_dict = self.tokenizer.question_encoder(input_questions, 
                                                     padding=True,
                                                     return_tensors="pt") 
        output_ids = self.model.generate(input_ids=input_dict["input_ids"],
                                         attention_mask=input_dict["attention_mask"],
                                         max_new_tokens=max_new_tokens)
        outputs = self.tokenizer.generator.batch_decode(output_ids, skip_special_tokens=True)
        return outputs

    def prediction_step_mcqa(self, batch, tokenizer):
        """
        Computes the mcqa prediction of the given question.

        Args:
            batch (`list` of `dict`):
                A list of dictionaries containing the input mcqa data for the DPO model.
                The data format is as follows:
                {
                    "question": str,
                    "choices": List[str],
                    "answer": str,
                }
            tokenizer (`PreTrainedTokenizerBase`): The tokenizer used to tokenize the input questions.
        Returns:
            output_dict (`dict`): A dictionary containing the model predictions given input questions.
        """
        output_dict = {"preds": []}

        # Transform dict to string
        input_questions = [f"question: {x['question']}\nchoices: {', '.join(x['choices'])}" 
                            for x in batch]
        outputs = self.prediction_step(input_questions)
        output_dict = [{"question": x['question'], 
                        "choices": x['choices'], 
                        "answer": x['answer'],
                        "preds" : y}
                        for x, y in zip(batch, outputs)]

        return output_dict