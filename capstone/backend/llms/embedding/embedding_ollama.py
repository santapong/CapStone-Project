import logging

from dataclasses import dataclass

from langchain_chroma import Chroma
from langchain_ollama.embeddings import OllamaEmbeddings


@dataclass
class OllamaEmbedder:
    model: str = None
    """_summary_
    """
    
    path: str = None
    """_summary_
    """ 

    collection_name: str = None
    """_summary_
    """
    
    def __post_init__(self):
        logging.info("Connect to LLAMA3.2 embedding")
        print()
        self.embeddings = OllamaEmbeddings(model='llama3.2')

    def store(self):
        logging.info()
        self.vector_store = Chroma(
            collection_name="example_collection",
            embedding_function=self.embeddings,
            persist_directory="./chroma_langchain_db",  # Where to save data locally, remove if not necessary
        )
    
    def collection(self):
        pass
        
if __name__ == '__name__':
    embeddings = OllamaEmbedder(model='llama3.2')
    embeddings.store()