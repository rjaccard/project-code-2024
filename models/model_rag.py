import torch 
import torch.nn as nn

from transformers import (
    AutoConfig,
    RagConfig,
    RagRetriever,
    RagSequenceForGeneration,
    T5Tokenizer,
    DPRQuestionEncoderTokenizer,
    RagTokenizer,
    
)
from huggingface_hub import HfFolder, Repository
from datasets import load_from_disk
import faiss


class RAG(nn.Module):
    """This class implements a RAG model, using a custom pre-trained sequence-to-sequence model as generator and a custom indexed dataset.
    
    Example usage:
    ==============
    
    # Configure the RAG model with your own generator and your own question encoder. 
    path_generator = path_to_the_generator
    path_dataset = path_to_the_indexed_dataset
    path_index = path_to_the_faiss_index
    path_rag_local = path_to_save_local_rag_model
    path_rag_hub = path_to_save_hub_rag_model
    auth_token = your_huggingface_auth_token
    device = "cuda" if torch.cuda.is_available() else "cpu"

    rag = RAG(
        path_generator, path_dataset, path_index, path_rag_local, path_rag_hub,
        configure_model=True, n_docs=5, max_combined_length=1024, device=device,
        push_model_to_hub=True, auth_token=auth_token
    )

    # Load RAG model
    path_rag = path_to_the_hub_rag_model
    path_dataset = path_to_the_indexed_dataset
    path_index = path_to_the_faiss_index
    device = "cuda" if torch.cuda.is_available() else "cpu"

    rag = RAG(
        path_rag_hub = path_rag, path_dataset = path_dataset, path_index = path_index,
        device=device, configure=False
    )
    """

    def __init__(self, path_generator="rjaccard/start2", 
                 path_dataset="datasets/rag/rag_dataset", 
                 path_index="datasets/rag/rag_dataset_index.faiss", 
                 path_rag_local="checkpoints/rag", 
                 path_rag_hub = "jaffolte/rag", auth_token=None, push_model_to_hub=False,
                 configure_model=False, n_docs=5, max_combined_length=1024, device="cuda",
                 **kwargs) :

        super().__init__()

        self.device = device
        
        # Path to the 3 components of the RAG model 
        self.path_generator = path_generator
        self.path_encoder = "facebook/dpr-question_encoder-single-nq-base"
        self.path_rag = "facebook/rag-sequence-nq"

        # Path to the dataset and its faiss index
        self.path_dataset = path_dataset
        self.path_index = path_index

        # Path to the local and hub RAG model
        self.path_rag_local = path_rag_local
        self.path_rag_hub = path_rag_hub

        # Parameters for pushing the model to hub 
        self.auth_token = auth_token
        self.push_model_to_hub = push_model_to_hub

        # Components of the RAG model
        self.model = None 
        self.tokenizer = None
        self.dataset = None

        # If model has not been configured yet, configure it with the desired components
        if configure_model :
            print('\n⌚ Configuring RAG model...')
            self.configure_model(n_docs, max_combined_length)

        # Load RAG model 
        print('⌚ Loading RAG model...')
        self.load_model()
        print('\n✅ Model Loaded !\n')


    def configure_model(self, n_docs, max_combined_length) :
        """Configure the RAG model, with the desired components :
        - generator : pre-trained sequence-to-sequence model 
        - retriever : pre-trained retriever model ("facebook/rag-sequence-nq")
        - question encoder : pre-trained encoder model ("facebook/dpr-question_encoder-single-nq-base")
        """
        # Set up the generator and the question_encoder in the RAG configuration
        generator_config = AutoConfig.from_pretrained(self.path_generator)
        encoder_config = AutoConfig.from_pretrained(self.path_encoder)

        # Set up the RAG configuration
        rag_config = RagConfig.from_pretrained(
            self.path_rag,
            generator = generator_config,
            question_encoder = encoder_config,
            n_docs = n_docs,
            max_combined_length = max_combined_length,
            output_retrieved=True,
        )

        # Set up the retriever with the indexed dataset
        dataset = load_from_disk(self.path_dataset)
        dataset.load_faiss_index("embeddings", self.path_index)

        retriever = RagRetriever.from_pretrained(
            self.path_rag, indexed_dataset=dataset
        )

        # Set up the RAG model 
        model = RagSequenceForGeneration.from_pretrained_question_encoder_generator(
            self.path_encoder,             
            self.path_generator,                               
            retriever=retriever, 
            config=rag_config,
        )

        # Set up the tokenizers 
        generator_tokenizer = T5Tokenizer.from_pretrained(self.path_generator)
        encoder_tokenizer = DPRQuestionEncoderTokenizer.from_pretrained(self.path_encoder)

        # Save the configured model
        model.save_pretrained(self.path_rag_local)
        generator_tokenizer.save_pretrained(self.path_rag_local + '/generator_tokenizer')
        encoder_tokenizer.save_pretrained(self.path_rag_local + '/question_encoder_tokenizer')

        if self.push_model_to_hub :
            print('⌚ Push model to Hub...')
            model.push_to_hub(self.path_rag_hub, use_auth_token=self.auth_token)
            print('\n✅ Model pushed !\n')

    def load_model(self) :
        """Load the pre-trained configured RAG model."""

        # Load dataset and retriever
        self.dataset = load_from_disk(self.path_dataset)
        self.dataset.load_faiss_index("embeddings", self.path_index)

        retriever = RagRetriever.from_pretrained(self.path_rag_hub, indexed_dataset=self.dataset)
       
        # Load RAG model
        self.model = RagSequenceForGeneration.from_pretrained(self.path_rag_hub, retriever=retriever)\
            .to(self.device)

        # Load tokenizer 
        self.tokenizer = RagTokenizer.from_pretrained(self.path_rag_hub)
  

    def retrieve_documents(self, questions) :
        """Retrieve the most similar documents to a batch of questions.
        
        Args:
            - questions : list of questions to retrieve documents for.

        Returns:
            - input_ids : token ids of the questions
            - attention_mask : attention mask of the questions
            - question_hidden_states : hidden states of the questions obtained from the question encoder
            - docs_dict : dictionary containing data on the retrieved documents.
        """

        # Tokenize questions
        inputs = self.tokenizer(questions, return_tensors="pt", truncation=True, max_length=512)
        input_ids, attention_mask = inputs["input_ids"].to(self.device), inputs["attention_mask"].to(self.device)

        # Encode questions
        question_hidden_states = self.model.question_encoder(input_ids, attention_mask=attention_mask)[0]

        # Retrieve documents 
        docs_dict = self.model.retriever(
            input_ids.cpu().numpy(),                            # Questions input_ids
            question_hidden_states.cpu().detach().numpy(),      # Encoded questions
            prefix = self.model.generator.config.prefix,    # For T5 generation 
            n_docs = self.model.config.n_docs,              # Number of documents to retrieve
            return_tensors = "pt"
        )

        # Compute similarity scores 
        doc_scores = torch.bmm(
            question_hidden_states.unsqueeze(1),               
            docs_dict["retrieved_doc_embeds"].float().transpose(1, 2).to(self.device)
        ).squeeze(1)

        docs_dict['scores'] = doc_scores

        return input_ids, attention_mask, question_hidden_states, docs_dict
    

    def print_retrieved_documents(self, questions) :
        """Print retrieved documents for questions.
        
        Args:
            - questions : list of questions to retrieve documents for.
        """
        # Retrieve documents
        _, _, _, docs_dict = self.retrieve_documents(questions)

        # Ids of retrieved docs
        doc_ids = docs_dict['doc_ids']

        for batch in range(len(questions)):
            print("================================================")
            print(f'❓ {questions[batch]}')
            print("================================================\n")

            for idx, doc_id in enumerate(doc_ids[batch]) :
                data = self.dataset[doc_id.item()]
                print(f'Title :\t {data["title"]} (Score = {docs_dict["doc_scores"][batch, idx] : .3f})')
                print(f'👉 {data["text"]}', end='\n')


    def generate(self, questions,
                 num_beams=2, do_sample=True, max_new_tokens=512, temperature=0.1, no_repeat_ngram_size=2, early_stopping=True) : 
        """Generate answers to questions using the RAG model.
        
        Args:
            - questions: list of questions to generate answers for.
            - num_beams : number of beams for beam search
            - do_sample : sample from the logits instead of using argmax
            - max_new_tokens : maximum number of tokens to generate
            - temperature : temperature for sampling
            - no_repeat_ngram_size : no repeat n-gram size
            - early_stopping : stop generation when all beam hypotheses finished

        Returns:
            - generated : list of generated answers for the questions.
        """

        # Retrieve most similar documents documents
        input_ids, attention_mask, question_hidden_states, docs_dict = \
            self.retrieve_documents(questions)

        generated = self.model.generate(
            input_ids = input_ids,                      # Questions token ids
            attention_mask = attention_mask,            # Questions attention mask
            context_input_ids = docs_dict['context_input_ids'].to(self.device),              # Retrieved documents token ids
            context_attention_mask = docs_dict['context_attention_mask'].to(self.device),    # Retrieved documents attention mask
            doc_scores = docs_dict['scores'],           # Similarity scores between question and documents
            do_deduplication = False,                   # Remove similar content between generated content from each document
            num_beams = num_beams,                      # Beam search param
            max_new_tokens = max_new_tokens,            # Generation max length
            temperature = temperature,                  # Temperature for sampling
            no_repeat_ngram_size = no_repeat_ngram_size,# No repeat n-gram size
            early_stopping = early_stopping,            # Stop generation when all beam hypotheses finished
            do_sample=do_sample,                        # Sample from the logits instead of using argmax
        )
        
        return self.tokenizer.batch_decode(generated, skip_special_tokens=True)



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

        ########################################################################
        # TODO: Please implement the prediction step that generates the prediction of the given MCQA question
        # ======================================================================
        # You need to return one letter prediction for each question.
        # ======================================================================
        
        # Addition text to guide the model for prediction
        start_text = "The following are multiple choice questions (with answers) about STEM. " 
        rag_text = "You are given additional context using a RAG database. Please, check the relevance of context before answering. Do not take the context into account if it is not relevant.\n\n"

        # Process each question-answer pair in the batch
        questions = batch['question']
        answers = batch['answer']

        for item in zip(questions, answers):
            
            # Tokenize the question.
            question = start_text + rag_text + item[0] + " " + self.tokenizer.generator.eos_token
            inputs = self.tokenizer(question, return_tensors="pt", padding="max_length", truncation=True, max_length=512).to(self.device)

            # Retrieve the options from the question
            letters_pattern = re.compile(r'\n([A-Z])\. ')
            matches = letters_pattern.findall(question.split('\nOptions:', 1)[1])

            decoder_start_token_id = self.rag_model.config.generator.decoder_start_token_id
            decoder_input_ids = torch.tensor([[decoder_start_token_id]]).to(device)
            
            # Retrieve the logits for each option
            with torch.no_grad():
                outputs = self.rag_model(**inputs, decoder_input_ids=decoder_input_ids)

            logits_list = [outputs.logits[0][0][self.tokenizer.generator(i)['input_ids'][0]] for i in matches]
            logits = torch.tensor(logits_list)

            # Get the probabilities of each option
            probs = torch.nn.functional.softmax(logits)

            # Create a dictionary to map indices to letters dynamically
            index_to_letter = {index: letter for index, letter in enumerate(matches)}

            # Get the predicted letter
            pred = index_to_letter[torch.argmax(probs).item()]
            output_dict["preds"].append(pred)

        torch.cuda.empty_cache()

        ########################################################################

        return output_dict