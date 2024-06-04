from transformers import (
    DPRContextEncoder, 
    DPRContextEncoderTokenizerFast
)

from datasets import (
    Dataset, 
    load_from_disk,
    Features, 
    Value, 
    Sequence
)

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

import json
import os 
import shutil
import faiss
import pandas as pd


class DocumentLoader : 
    """This class creates an indexed dataset from a collection of markdown documents.
    
    Usage example:
    ============== 
    document_loader = DocumentLoader()
    document_loader.load_document(path_to_your_md_file)
    
    # Create the dataset (containing chunks of document)
    dataset = document_loader.create_dataset()

    # Compute embeddings
    dataset = document_loader.compute_embeddings(dataset)

    # Save dataset
    document_loader.save_dataset(dataset, path_save_folder=path_to_dataset_folder)

    # Create faiss index 
    document_loader.index_dataset(dataset, path_index=path_to_index_folder)
    
    """

    def __init__(self, chunk_size=800, chunk_overlap=80, 
                 path_ctx_encoder="facebook/dpr-ctx_encoder-single-nq-base",
                 device="cuda"
                ) :

        # Recursive Chunking
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size, chunk_overlap=chunk_overlap
        )

        # Initialize the DPR context encoder
        self.ctx_tokenizer = DPRContextEncoderTokenizerFast.from_pretrained(path_ctx_encoder)
        self.ctx_encoder = DPRContextEncoder.from_pretrained(path_ctx_encoder).to(device=device)
        
        self.device = device
        self.documents = []         

    def load_document(self, path) :
        """Load a markdown document and split it into chunks
        
        Args: 
            - path (str): path to the markdown document
        """

        loader = TextLoader(path, autodetect_encoding=True)
        documents = loader.load()

        documents = self.text_splitter.split_documents(documents)

        # Set id of the document as its path (course name + chapter title) + chunk id
        documents = self.update_metadata(documents)

        documents = [
            {"title" : doc.metadata['id'],
            'text' : doc.page_content}
            for doc in documents
        ]
        self.documents.extend(documents)
    
    def get_title(self, file_path) :
        """Extract the title of the document from its path"""
        title = ''.join(file_path.split('\\')[1])
        title = ''.join(title.split('.')[0]).replace('_', ' ').replace('-', ' - ')
        return title

    def update_metadata(self, documents) :
        """Add the chunk id to the path of the document to create the title
        
        Args:
            - documents (list): list of chunked documents
        
        Returns:
            - new_docs (list): list of documents with updated metadata
        """
        new_docs = []
        for idx, doc in enumerate(documents) :
            doc.metadata = {"id" : f"{self.get_title(doc.metadata['source'])}:{idx}"}
            new_docs.append(doc)
        return new_docs 
    
    def create_dataset(self) :
        """Transform the list of documents into a huggingface dataset."""
        df = pd.DataFrame(self.documents)
        dataset = Dataset.from_pandas(df)

        return dataset
        
    def embeddings(self, documents):
        """Compute the DPR embeddings of document passages"""
        input_ids = self.ctx_tokenizer(
             documents["text"], padding="max_length", truncation=True, max_length=512, return_tensors="pt"
        )["input_ids"]
        
        embeddings = self.ctx_encoder(input_ids.to(device=self.device), return_dict=True).pooler_output
        return {"embeddings": embeddings.detach().cpu().numpy()}
    
    def compute_embeddings(self, dataset) :
        """Compute the embeddings for all documents in the dataset"""
        new_features = Features(
            {"text": Value("string"), "title": Value("string"), "embeddings": Sequence(Value("float32"))}
        )  
        dataset = dataset.map(self.embeddings, batched=True, batch_size=16, features=new_features)
        return dataset
    
    def save_dataset(self, dataset, path_save_folder="datasets/rag/rag_dataset") : 
        """Save the dataset to disk
        
        Args:
            - dataset (Dataset): dataset to save
            - path_save_folder (str): path to the folder where the dataset will be saved
        """
        # Remove folder (if it exists)
        if os.path.exists(path_save_folder):
            try:
                shutil.rmtree(path_save_folder)
            except Exception as e:
                print(f'Error: {e}') 
        
        dataset.save_to_disk(path_save_folder)

    def index_dataset(self, dataset, 
                      path_index='datasets/rag/rag_dataset_index.faiss', 
                      embedding_dim=768,
                      nb_links=128,
                      ):
        """Index the dataset with HNSW (Hierarchical Navigable Small World Graphs)
        
        Args:
            - dataset: dataset to index
            - path_index: path to save the index
            - embedding_dim: dimension of embeddings 
            - nb_links: number of links in the HNSW graph
        """
        # Create the FAISS index
        index = faiss.IndexHNSWFlat(embedding_dim, nb_links, faiss.METRIC_INNER_PRODUCT)
        # Set custom index
        dataset.add_faiss_index(column="embeddings", custom_index=index)
        # Save the index
        dataset.get_index("embeddings").save(path_index)

