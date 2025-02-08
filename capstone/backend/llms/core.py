import os
import logging

from typing import (
    List, 
    Union, 
    Dict,
    )
from typing_extensions import Self
from langchain_postgres import PGVector
from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
from langchain_text_splitters import (
    TextSplitter, 
    RecursiveCharacterTextSplitter
    )
from langchain_experimental.text_splitter import SemanticChunker
from langchain_ollama import (
    OllamaEmbeddings, 
    OllamaLLM
    )

from capstone.backend.llms.prompt_template import prompt

# Get from ENV
LLM_MODEL = os.getenv("LLM_MODEL",default= "llama3.2")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL",default='bge-m3')
COLLECTION_NAME = os.getenv("COLLECTION_NAME",default="langchain")

# For Chromadb server settings ( Using postgresql )
# client_settings = {
#     "chroma_server": "http://localhost:8000",  # Chroma server URL
#     "database": os.getenv("DATABASE_TYPE",default="postgresql"), 
#     "postgres_host": os.getenv("DATABASE_HOST", default="localhost"), 
#     "postgres_port": os.getenv("DATABASE_PORT",default="5432"), 
#     "postgres_user": os.getenv("DATABASE_USERNAME",default="postgres"),  
#     "postgres_password": os.getenv("DATABASE_PASSWORD",default="postgres"),  
#     "postgres_db": os.getenv("DATABASE_NAME",default="chromadb")  
# }
# Using For Local
PERSIST_DIR = os.getenv("PERSIST_DIR",default="database/vector_history")

# TODO: Reseacrh how to make it easy calls.
# I need it will chain calling
class RAGModel:
    def __init__(self):
        self.__llm = OllamaLLM(model=LLM_MODEL)
        self.__vector_store = self.__chroma_connect()

    # Pre Retrieval Process.
    def pre_retrieval(
            self, 
            question
            ):
        
        # TODO: Fix this shit
        # Rewritten Query Prompt
        query_rewrite_prompt = f"""You are a helpful assistant that takes a
        user's query and turns it into a short statement or paragraph so that
        it can be used in a semantic similarity search on a vector database to
        return the most similar chunks of content based on the rewritten query.
        Please make no comments, just return the rewritten query.
        \n\nquery: {question}\n\nai: """

        answer = self.__llm.invoke(query_rewrite_prompt)

        return answer

    def __chroma_connect(self):
        return Chroma( 
            collection_name=COLLECTION_NAME,
            embedding_function=OllamaEmbeddings(model=EMBEDDING_MODEL),
            persist_directory=PERSIST_DIR
            # **client_settings
            )

    # Internal Split Text
    def __split_text(self,
                    contents:str,
                    metadatas: Dict[str,str],
                    chunk_size:int = 1000,
                    separaters: str ='/n'
                    ):
        # Splitter text API contents.
        splitter = RecursiveCharacterTextSplitter(
            chunk_size = chunk_size,
            chunk_overlap = chunk_size*0.25,
            separators=separaters
            )
        texts =  splitter.split_text(contents)
        documents = splitter.create_documents(
            texts=texts,
            )

        return documents

    # Load Document From API
    async def aload_from_API(self,
                  contents:Union[Dict[str,str],str],
                  metadatas: Dict[str,str],
                  chunk_size:int = 1000,
                  )-> List[Document]:
        
        # Split text from API
        documents = self.__split_text(
            contents=contents,
            metadatas=metadatas)
        
        # Add Document to Vector store.
        self.__vector_store.add_documents(
            documents=documents,
            )

        return documents

    # Load Multiple Documents and Sematics Chunk.
    def sematic_load():
        pass

    def invoke(
            self, 
            question:str,
            expand:bool = False,
            ):
        if not expand:
            question = self.__pre_retrieval(question)

        # Call Retriever
        self.retriever = self.__vector_store.as_retriever()

        # Create Chains
        combine_docs_chain = create_stuff_documents_chain(
            prompt=prompt,
            llm=self.__llm
        )

        # Create Retrieval Chains
        retrieval_chains = create_retrieval_chain(
            retriever=self.retriever,
            combine_docs_chain=combine_docs_chain
            )
        
        return retrieval_chains.invoke({"input": question})

if __name__ == "__main__":
    test = RAGBase().pre_retrieval(question="What is the capital of France?")
    print(test)