import os
import logging
from dotenv import load_dotenv

load_dotenv()

from typing import Optional, List, Union
from dataclasses import dataclass

from langchain.text_splitter import (
    CharacterTextSplitter,
    RecursiveCharacterTextSplitter
    )

from langchain_core.documents import Document
from langchain_community.document_loaders.base import BaseLoader
from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    WebBaseLoader
    )

from capstone.backend.llms.utils.exception import CustomErrorHandler

"""
# NOTE:
# LoaderManager use for manager and handle, when loading all of file type using of Loader from langchain.
#
"""
# TODO: It need to download to temp and train model when complete delete that file ??
class LoaderManager:
    
    # Not use
    def __init__(self):
        pass

    # This is will run inside of this Class not need to use it.
    # Split text to Chunk.
    def __split_text(self,
                     loader: BaseLoader,         
                     docs: List[Document] = None,
                     chunk: int = None,
                     chunk_overlap: int = None
                     ) -> List[Document]:
        
        # Text splitter from Loader.
        text_splitter = CharacterTextSplitter(
            chunk=chunk,
            chunk_overlap=chunk_overlap,
            separator="/n"
        )
        
        return text_splitter.split_documents(documents=docs)
    
    # FIXME: Need to fix Loader pdf. and need to test.
    # Load PDF from file_path.
    def load_pdf(self,
                 file_path: str = None,
                 chunk: int = 100,
                 chunk_overlap: int = 0
        ) -> Union[List[Document],Document]:
        if not file_path:
            raise FileNotFoundError(f"Need file_path to run")
        
        # Read PDF page.
        pages = []
        self.loader = PyPDFLoader(file_path=file_path)
        for page in self.loader.lazy_load():
            pages.append(page)

        # Split text to chunk
        self.__split_text(loader=self.loader,
                          docs=pages,
                          chunk=chunk,
                          chunk_overlap=chunk_overlap)
        

    # Load Text from file_path.
    def load_text(self):
        pass

    # Load Content of website.
    def load_website(self):
        pass

    # Load content from API.
    def load_file(self):
        pass
    
    # Display all of document content.
    def get_docs(self) -> str:
        return self.docs
    




if __name__ == '__main__':
    test = LoaderManager()

    test.__split_text(PyPDFLoader)