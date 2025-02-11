import os
import logging

from typing_extensions import Self
from typing import (
    List, 
    Union, 
    Dict,
    )

from langchain_chroma import Chroma
from langchain_postgres import PGVector
from langchain_core.documents import Document
from langchain.chains.retrieval import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
    )
from langchain_experimental.text_splitter import SemanticChunker
from langchain_ollama import (
    OllamaEmbeddings, 
    OllamaLLM
    )

from capstone.backend.llms.prompt_template import (
    rag_prompt,
    pre_retrieval
    )

# Get from ENV
LLM_MODEL = os.getenv("LLM_MODEL",default= "llama3.2")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL",default='bge-m3')
COLLECTION_NAME = os.getenv("COLLECTION_NAME",default="langchain")
# Persist Directory
PERSIST_DIR = os.getenv("PERSIST_DIR",default="database/vector_history")

# TODO: Learn About Websearch
# RAG Class model.
class RAGModel:
    def __init__(
            self,
            temperature: float = 0.5
            ):
        self.__vector_store = self.__chroma_connect()
        self.__llm = OllamaLLM(
            model=LLM_MODEL,
            temperature=temperature,
            )

    # Pre Retrieval Process.
    def __pre_retrieval(
            self, 
            question
            ):
        
        # TODO: Fix this shit
        # Rewritten Query Prompt
        prompt = pre_retrieval(question=question)
        return self.__llm.invoke(prompt)

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

    # Query to LLMs.
    def invoke(
            self, 
            question:str,
            ):

        # Call Retriever
        self.retriever = self.__vector_store.as_retriever(
            search_type="mmr",
            search_kwargs={'k': 6, 'lambda_mult': 0.5}
            )

        # Create Chains
        combine_docs_chain = create_stuff_documents_chain(
            prompt=rag_prompt(),
            llm=self.__llm
        )

        # Create Retrieval Chains
        retrieval_chains = create_retrieval_chain(
            retriever=self.retriever,
            combine_docs_chain=combine_docs_chain
            )

        return retrieval_chains.invoke({"question": question,"input":""})
    

# Make for FastAPI Depends 
def get_RAG():
    yield RAGModel()

if __name__ == '__main__':
    test = RAGModel()
    print(test.invoke("What is Automation")) 