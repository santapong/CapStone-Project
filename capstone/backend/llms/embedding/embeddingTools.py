import os 

from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

from typing import Optional

from langchain_ollama import OllamaEmbeddings
from langchain_chroma import vectorstores, Chroma


# TODO: Implement to use with dataclass.
class EmbeddingManager:
    def __init__(self, model: Optional[str]='llama3.2'):
        # Set Embedding model and Prepare Vector Store.
        print(f"Create connection to embedding model '{model}' and create vector database using Chromadb")
        self.embeddings = OllamaEmbeddings(model=model)
        self.vector_store = Chroma(
            collection_name="example_data",
            embedding_function=self.embeddings,
            persist_directory='capstone/backend/database/vector_database'
        )
    
if __name__ == "__main__":
    test = EmbeddingManager()