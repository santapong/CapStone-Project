import os
import logging

from typing import List
from typing_extensions import Self

from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
from langchain_text_splitters import (
    TextSplitter, 
    RecursiveCharacterTextSplitter
    )
from langchain_ollama import (
    OllamaEmbeddings, 
    OllamaLLM
    )

# Gen from ENV
LLM_MODEL = os.getenv("LLM_MODEL",default= "llama3.2")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL",default='bge-m3')

# For Chromadb server settings ( Using postgresql )
client_settings = {
    "chroma_server": "http://localhost:8000",  # Chroma server URL
    "database": os.getenv("DATABASE_TYPE",default="postgresql"), 
    "postgres_host": os.getenv("DATABASE_HOST", default="localhost"), 
    "postgres_port": os.getenv("DATABASE_PORT",default="5432"), 
    "postgres_user": os.getenv("DATABASE_USERNAME",default="postgres"),  
    "postgres_password": os.getenv("DATABASE_PASSWORD",default="postgres"),  
    "postgres_db": os.getenv("DATABASE_NAME",default="chromadb")  
}
# Using For Local
# PERSIST_DIR = os.getenv("PERSIST_DIR",default="/database/vector_history")

# I need it will chain calling
class RAGBase:
    def __init__(self):
        pass

    def __split_text():
        pass

    def sematic_load():
        pass

    def invoke():
        pass