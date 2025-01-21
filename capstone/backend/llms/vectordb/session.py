import os 
import logging
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

from typing import Optional, Union

from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_core.vectorstores.base import VectorStore

logging.getLogger(__name__)

# TODO: Implement to use with dataclass.
class VectorDBConnect:

    def __init__(self, 
                embedding_model: Optional[str]='bge-m3',
                collection_name :str = 'vector_database',
                persist_directory: str = 'capstone/backend/database/vector_database'
                ) -> None:
        
        # Set Embedding model and Prepare Vector Store.
        print(f"Create connection to embedding model '{embedding_model}' and create vector database using Chromadb")
        self.embeddings = OllamaEmbeddings(model=embedding_model)
        self.vector_store = Chroma(
            collection_name=collection_name,
            embedding_function=self.embeddings,
            persist_directory=persist_directory
        )
    
    def add_document(self, 
        docs: Union[list, str]
        )->None:
        print("start add documents")
        self.vector_store.add_documents(docs)

    def similar_search(self):
        pass

    def similar_with_score(self):
        pass

    def from_document(self):
        pass

    def retreiver(self):
        pass
    
if __name__ == "__main__":
    session = VectorDBConnect()
