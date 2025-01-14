import os 
from dotenv import load_dotenv

load_dotenv()

from dataclasses import dataclass
from typing import Optional, List

from langchain_community.document_loaders import PyPDFLoader

# Can it use with Text Spliter
# TODO: Implement to use with dataclass
class PDFLoaderManager:

    def __init__(self, file_path: str) -> None:
        print(f"Loading.. {file_path}")
        self.loader = PyPDFLoader(file_path=file_path)

    def __splitter(self):
        pass

    def get_PDF(self):

        # Split to File to to Page
        pages = []
        for page in self.loader.lazy_load():
            pages.append(page)
        return pages



if __name__ == '__main__':

    # Get PDF file path from .env
    file_path = os.getenv("PDFLOADER")
    test = PDFLoaderManager(file_path=file_path)
    
    # print(test.get_PDF()[0].metadata)
    """ result
    """
    print(test.get_PDF()[0].page_content)