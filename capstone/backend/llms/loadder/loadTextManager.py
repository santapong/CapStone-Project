import os
from dotenv import load_dotenv

load_dotenv()

from typing import Optional
from dataclasses import dataclass

from langchain_community.document_loaders import TextLoader

# TODO: Implement to use with Dataclass
class LoadTextManager:
    def __init__(self, file_path: str=None) -> None:
        print(f"Loading.. {file_path}")
        self.loader = TextLoader(file_path=file_path)
# TODO: See Lazy_load
    def get_Text(self):
        return self.loader.load()
        

if __name__ == '__main__':

    
    file_path = os.getenv('TEXTLOADER')
    test = LoadTextManager(file_path=file_path)

    test.get_Text()
    """result 
    [
        Document(metadata={'source': './document/test.txt'}, page_content='This is Text Loader')
    ]
    """ 
