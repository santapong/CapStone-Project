import io
import os
import json
import time
import logging

from abc import ABC
from pypdf import PdfReader
from dotenv import load_dotenv
from typing_extensions import Self
from typing import (
    List, 
    Dict,
    Union,
    Optional,
    )

from langchain_core.documents import Document
from langchain_core.language_models import BaseLLM

from langchain_chroma.vectorstores import Chroma

from langchain.text_splitter import CharacterTextSplitter, RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings, OllamaLLM
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    WebBaseLoader
    )

from capstone.backend.llms.prompt_template import prompt
from capstone.backend.llms.utils.exception import RAGHandle
from capstone.backend.llms.vectordb.session import VectorDBConnect
# from capstone.backend.llms.loadder.LoaderManager import LoaderManager

load_dotenv()
logging.getLogger(__name__)

"""
################ TAKE NOTE #################
#   
#   Consept of This file is to manage all 
#   of process that use with RAG.
#
#
############################################
"""

# Design RAG system before do this one.

# Define Class for Retrieval-Augmented Generation (RAG)
## Using Inheritance of LoadManger, ChatModel
#TODO: Make it when call it easy to call.
class RAGmodel:

    """
    RAG Class for LLM.

    """
    
    # Set Default value in ENV
    # TODO: Make read default value from ENV
    def __init__(self):
        self.__llm = None
        self.__embeddings = None
        self.__vector_store = None

#TODO: Make it as a Internal Method
## Document Splitter
    def __split_document(self,
                       documents: Union[List[Document], Document] = None,
                       chunk:int = 400,
                       chunk_overlap = 10,
                       separators:str ='/n'
                       ) -> List[Document]:
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk, 
            chunk_overlap=chunk_overlap,
            separators=separators)
        documents = splitter.split_documents(documents=documents)

        return documents
    
# Make it can handle Metadata
# Split text from API.
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


## Load PDF from local file.
### TODO: Make it will save in vector database.
    def load_PDF(self,
                 file_path:str = None,
                 metadata:Dict = None
                 ) -> Union[List[Document], Document]:
            
        # Extract PDF file.
        pages = []
        loader = PyPDFLoader(file_path=file_path)
        for page in loader.lazy_load():
            page.metadata.update(metadata)
            pages.append(page)
        
        # Add Document to Vector store.
        documents = self.__split_document(documents=pages)
        self.__vector_store.add_documents(documents=documents)

        return pages

# TODO: Make it use Retrieval.
## Load Text file.
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
    
## Load Website content.
## NOTE Beware the law.
    def load_Webbase(self):

        documents = WebBaseLoader()

        return documents
        
    
# TODO: Make it is internal method
## Stored VectorDB & Retrieval.

## Post Retreieval
    def __post_retreieval(self):
        pass

## Set LLM model.
    def setModel(self, 
        model:str='llama3.2',
        temparature: float=0.8,
        top_p: float=0.8,
        top_k: float=None,
        cache: str=None,
        output_type: str='',
        **kwargs
        ) -> Self :

        self._llm = OllamaLLM(model=model,
                            #   temperature=temparature,
                            #   top_k=top_k,
                            #   top_p=top_p,
                            #   cache=cache,
                            #   format=output_type
                            )
        return self
    

## Setting Embeddings model
    def setEmbeddings(self, 
                    embeddings_model:str = 'bge-m3',
                    ) -> Self:

        # Setting Embedding model
        logging.info(f"Using {embeddings_model} as embedding model.")
        self.__embeddings = OllamaEmbeddings(model=embeddings_model)
        return self

# Vector Database
    def setVectorDB(self,
                    collection_name: str = os.getenv("COLLECTION_NAME", default='langchain'),
                    persist_directory: str = os.getenv("VECTORDB_PATH"),

                    )-> Self:
        
        # Create vector_store
        self.__vector_store = Chroma(
            embedding_function=self.__embeddings,
            collection_name=collection_name,
            persist_directory=persist_directory
        )
        return self


## Generation
    def invoke(self, 
               question: str = None):
               
        # Create Retriever from ChromaDB
        retriever = self.__vector_store.as_retriever() 

        combine_docs_chain = create_stuff_documents_chain(
            llm=self._llm,
            prompt=prompt
        )

        chains = create_retrieval_chain(
            retriever=retriever,
            combine_docs_chain=combine_docs_chain
            )

        return chains.invoke({"input":question})

## Performance Zone


## Evaluation

if __name__ == '__main__':

    # Load JSON file
    with open("./evaluation/test_knowledge.json", "r") as f:
        json_data = json.load(f)

    print(json_data[0]["prompt"])

    # query = "Can you tell me about few shot"

    # file_path = os.getenv("PDFLOADER")

    # PERSIST_DIRECTORY ='capstone/backend/database/vector_database'

    # test = RAGmodel().setEmbeddings().setModel().setVectorDB()

    # docs = test.load_PDF(file_path=file_path,
    #                      metadata={"test":"test"})

    # start_time = time.time()
    # answer = test.invoke(question="")
    # time_usage = time.time() - start_time

    # with open("answer.txt", "a") as f: 
    #     f.write(answer['answer'])