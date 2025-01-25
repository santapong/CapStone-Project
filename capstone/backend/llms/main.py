import logging

from abc import ABC
from pypdf import PdfReader
from dotenv import load_dotenv
from typing import (
    List, 
    Dict,
    Union,
    )
from typing_extensions import Self


from langchain_core.documents import Document
from langchain_core.language_models import BaseLLM

from langchain_chroma.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings, OllamaLLM

from langchain.text_splitter import CharacterTextSplitter, RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    WebBaseLoader
    )

from capstone.backend.llms.prompt_template import prompt
from capstone.backend.llms.vectordb.session import VectorDBConnect
from capstone.backend.llms.utils.exception import RAGHandle
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
class RAGmodel:

    def __init__(self):
        self.__llm = None
        self.__embeddings = None

 
## Load PDF File 
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
        
        return pages
    
# TODO: Make it is internal method
## Stored VectorDB & Retrieval.
    def __retreieval(self,
                   documents:Union[List[Document], Document] = None,
                   collection_name:str = None,
                   collection_metadata:Dict =None,
                   persist_directory:str =None):
        logging.info(f"Retreie {documents}")

        # Insert Document to VectorDatabase
        self.vector_store = Chroma.from_documents(documents=documents,
                                         persist_directory=persist_directory,
                                         collection_name=collection_name,
                                         collection_metadata=collection_metadata,
                                         embedding=self.__embeddings)

## Post Retreieval
    def __post_retreieval(self):
        pass

## Re-rank Process
    def __rerank(self):
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
    

## Setting Vector Database
    def setEmbeddings(self, 
                    embeddings_model:str = 'bge-m3',
                    ) -> Self:
        print("Test embedding")

        # Setting Embedding model
        logging.info(f"Using {embeddings_model} as embedding model.")
        self.__embeddings = OllamaEmbeddings(model=embeddings_model)
        return self

#TODO: Make it as a Internal Method
## Document Splitter
    def __split_document(self,
                       documents: Union[List[Document], Document] = None,
                       chunk:int = 400,
                       chunk_overlap = 10,
                       seperator:str ='/n'
                       ) -> List[Document]:
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk, chunk_overlap=chunk_overlap)
        docs = text_splitter.split_documents(documents=documents)

        return docs

## Generation
    def invoke(self, 
               question: str = None):
               
        # Create Retriever from ChromaDB
        retriever = self.vector_store.as_retriever() 

        combine_docs_chain = create_stuff_documents_chain(
            llm=self._llm,
            prompt=prompt
        )

        chains = create_retrieval_chain(retriever=retriever,
                                        combine_docs_chain=combine_docs_chain)

        return chains.invoke({"input":question})

## Performance Zone


## Evaluation

if __name__ == '__main__':
    import os

    query = "Can you tell me about few shot"

    file_path = os.getenv("PDFLOADER")

    PERSIST_DIRECTORY ='capstone/backend/database/vector_database'

    test = RAGmodel().setEmbeddings().setModel()

    # docs = test.load_PDF(file_path=file_path,
    #                      metadata={"test":"test"})
    
    

    # test.retreieval(documents=docs,
    #                 collection_name="test",
    #                 collection_metadata={"test":"test"},
    #                 persist_directory=PERSIST_DIRECTORY)

    # anwser = test.invoke(question="show me your knowledge")['answer']

    # with open("anwser.txt", "a") as f:
    #     f.write(anwser)