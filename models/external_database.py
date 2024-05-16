from datasets import load_dataset, load_from_disk

from transformers import DPRContextEncoder, DPRContextEncoderTokenizerFast

from typing import List, Optional
from functools import partial

import torch
import faiss


class ExternalDatabase : 

    def __init__(self,
                 path_ctx_encoder="facebook/dpr-ctx_encoder-multiset-base",
                 device="cuda") :

        self.ctx_tokenizer = DPRContextEncoderTokenizerFast.from_pretrained(path_ctx_encoder)
        self.ctx_encoder = DPRContextEncoder.from_pretrained(path_ctx_encoder).to(device=device)
        self.device = device
    
    # ==================== #
    #   Create dataset     #
    # ==================== #

    def create_dataset(self, path_to_csv):
        """Create a dataset from a csv file."""
        dataset = load_dataset(
            "csv", data_files=[path_to_csv], split="train", delimiter=";", column_names=["title", "text"]
        )
        return dataset
    
    def split_text(self, text, n=100, character=" "):
        """Split the text into chunks of 100 tokens."""
        text = text.split(character)
        return [character.join(text[i : i + n]).strip() for i in range(0, len(text), n)]

    def split_documents(self, documents):
        """Split documents into passages"""
        titles, texts = [], []
        for title, text in zip(documents["title"], documents["text"]):
            if text is not None:
                splited_text = self.split_text(text)
                for passage in splited_text:
                    titles.append(title if title is not None else "")
                    texts.append(passage)
        return {"title": titles, "text": texts}

    def compute_embeddings(self, documents):
        """Compute the DPR embeddings of document passages"""
        input_ids = self.ctx_tokenizer(
            documents["title"], documents["text"], truncation=True, padding="longest", return_tensors="pt"
        )["input_ids"]
        embeddings = self.ctx_encoder(input_ids.to(device=self.device), return_dict=True).pooler_output
        return {"embeddings": embeddings.detach().cpu().numpy()}
    
    def save_dataset(self, dataset, path_save_folder):
        """Save the dataset to a folder"""
        dataset.save_to_disk(path_save_folder)

    def load_dataset(self, path_dataset):
        """Load the dataset from a folder"""
        return load_from_disk(path_dataset)

    # ==================== #
    #    Index dataset     #
    # ==================== #

    def index_dataset(self, dataset, path_index,
                      embedding_dim=768,
                      nb_links=128,
                      ):
        """Index the dataset with HNSW (Hierarchical Navigable Small World Graphs)"""
        # Create the FAISS index
        index = faiss.IndexHNSWFlat(embedding_dim, nb_links, faiss.METRIC_INNER_PRODUCT)
        # Set custom index
        dataset.add_faiss_index(column="embeddings", custom_index=index)
        # Save the index
        dataset.get_index("embeddings").save(path_index)

    def load_index(self, path_index, dataset):
        """Load the index."""
        return dataset.load_faiss_index("embeddings", path_index)
