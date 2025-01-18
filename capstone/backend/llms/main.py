import os 
import logging

from dotenv import load_dotenv
from abc import abstractmethod, ABC

from langchain_core.documents import Document
from langchain_core.embeddings import Embeddings
from langchain_core.language_models import BaseLLM

from langchain_ollama import OllamaEmbeddings, OllamaLLM

# Maybe not use
from capstone.backend.llms.core.models import ChatModel

from capstone.backend.llms.vectordb.session import VectorDBConnect
from capstone.backend.llms.prompt_teamplate.prompt_template import (
    few_shot_prompt_template,
    few_shot_input_variable,
    test_prompt_template,
    test_prompt_input_variable,
    zero_shot_input_variable,
    zero_shot_prompt_template)

from capstone.backend.llms.loadder.LoaderManager import LoaderManager
from capstone.backend.llms.utils.exception import RAGHandle

load_dotenv()

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

# TODO: Make more function.

# Define Class for Retrieval-Augmented Generation ( RAG. )
## Using Inheritance of LoadManger, ChatModel
class RAGmodel(ABC, LoaderManager):


    ## Set LLM model.
    def setModel(self, 
                 model:str='llama3.2',
                 temparature: int=None,
                 top_p: int=None,
                 top_k: int=None,
                 cache: str=None,
                 output_type: str=None,
                 **kwargs
                 ) -> BaseLLM:
        """
        To set llm model to use in RAG


        Args:
            model (str, optional): LLM model that you need to use. Defaults to 'llama3.2'.
            temparature (int, optional): temperature for model. Defaults to None.
            top_p (int, optional): top_p parameter. Defaults to None.
            top_k (int, optional): top_k parameter. Defaults to None.
            cache (str, optional): cache for model. Defaults to None.
            output_type (str, optional): format output such as json, normal text. Defaults to None.

        Returns:
            BaseLLM: LLM model
        """
        self._llm = OllamaLLM(model=model,
                              temperature=temparature,
                              top_k=top_k,
                              top_p=top_p,
                              cache=cache,
                              format=output_type)
        return self._llm

    # Set embedding model.
    def setEmbedding(self,
                     model:str='bge-m3',
                     base_url:str='',
                     **client_kwarg
                     ) -> Embeddings:
        """

        Args:
            model (str, optional): embedding model. Defaults to ''.
            base_url (str, optional): base url of embedding model like Ollama. Defaults to ''.

        Returns:
            Embeddings: Embedding model.
        """
        self._embeddings = OllamaEmbeddings(model=model,
                                            base_url=base_url,
                                            client_kwargs=client_kwarg)
        return self.__embeddings

# Load Document & Split_text
## Using LoaderManger to Handle PDF, Website, Text, API Upload.
    def load(self,
             type:str=None,
             file_path:str = None,
             )-> Document:
        """

        Args:
            type (str, optional): Using for API. Defaults to None.
            file_path (str, optional): Using for local machine. Defaults to None.

        Returns:
            Document: Document class.
        """
        
        # Loading PDF
        pdf_file = self.load_pdf(file_path=file_path)
        # Loading Content of Website

        # Loading Text

        # Loading from API Upload

        return self.load_pdf

    # Return Document.
    def display_document(self):
        return self.get_docs()

## Embedding
    def __embeddings_document(self):
        self._embeddings
        


## Stored VectorDB & Retreieval
    def __vectordb_process(self):
        pass

## Post Retreieval
    def __post_retreieval(self):
        pass

## Re-rank Process
    def __rerank(self):
        pass

## Generation


## Performance Zone


## Evaluation
