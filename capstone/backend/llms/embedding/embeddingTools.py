import os 

from dataclasses import dataclass
from dotenv import load_dotenv

from capstone.backend.llms.loadder import WebLoaderManager

load_dotenv()

from typing import Optional, Union

from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma

# TODO: Implement to use with dataclass.
class EmbeddingManager:
    def __init__(self, model: Optional[str]='llama3.2')-> Chroma:
        # Set Embedding model and Prepare Vector Store.
        print(f"Create connection to embedding model '{model}' and create vector database using Chromadb")
        self.embeddings = OllamaEmbeddings(model=model)
        self.vector_store = Chroma(
            collection_name="example_data",
            embedding_function=self.embeddings,
            persist_directory='capstone/backend/database/vector_database'
        )
    
    def add_document(self, docs: Union[list, str]):
        print("start add documents")
        self.vector_store.add_documents(docs)
    
if __name__ == "__main__":
    
    URL = ["https://www.example.com/", "https://google.com"]
    
    WebbaseLoadManager = WebLoaderManager(URL=URL)

    documents = [_ for _ in WebbaseLoadManager.get_URL()]
    print(documents)

    EmbeddingManagers = EmbeddingManager()

    EmbeddingManagers.add_document(documents)