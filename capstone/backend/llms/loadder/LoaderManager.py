import os
import logging
from dotenv import load_dotenv

load_dotenv()

from typing import Optional, List, Union
from dataclasses import dataclass



from langchain.text_splitter import (CharacterTextSplitter,
                                     RecursiveCharacterTextSplitter)

from langchain_core.documents import Document
from langchain_community.document_loaders.base import BaseLoader
from langchain_community.document_loaders import (PyPDFLoader,
                                                  TextLoader,
                                                  WebBaseLoader)

from capstone.backend.llms.utils.exception import ErrorHandler

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

    # Load PDF from file_path.
    def load_pdf(self,
                 file_path: str = None,
                 chunk: int = 100,
                 chunk_overlap: int = 0
        ) -> Union[List[Document],Document]:
        if file_path:
            raise FileNotFoundError(f"Need file_path to run")
        self.loader = PyPDFLoader(file_path=file_path)
        
    # Load Text from file_path.
    def load_text(self):
        pass

    # Load Content of website.
    def load_website(self):
        pass
    
    # Display all of document content.
    def get_docs(self) -> Union[]:
        return self.docs
    
    # This is will run inside of this Class not need to use it.
    # Split text to Chunk.
    def __split_text(self,
                     loader: BaseLoader,         
                     docs: Document = None,
                     chunk: int = None,
                     chunk_overlap: int = None
                     ) -> List[Document]:
        pass



if __name__ == '__main__':
    test = LoaderManager()

    test.__split_text(PyPDFLoader)