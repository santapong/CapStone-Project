import os
from dotenv import load_dotenv

load_dotenv()

from abc import abstractmethod
from typing import Optional
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter

# TODO: Need more update.
# Text Splitter to make easy to upload data.
def splitterText(
        chunk_size: Optional[int] = 100, 
        chunk_overlap: Optional[int] = 0, 
        seperator: str ='\n',
        ) -> CharacterTextSplitter :

    text_splitter = CharacterTextSplitter(chunk_size=chunk_size, 
                                          chunk_overlap=chunk_overlap, 
                                          separator=seperator)
    
    return text_splitter


# TODO: Create splitter manager that can split all of any kind of source.
class SplitterManager:

    def __init__(self):
        pass

    def split(self):
        pass

# Tests Zone.
if __name__ == '__main__':

    file_path = os.getenv('TEXTLOADER')

    # Declare Chunk properties
    chunk_size = 20
    chunk_overlap = 0

    # it will first find first 20 character then it will make the next chunk at the closest separator
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )

    loader = TextLoader(file_path=file_path)
    docs = loader.load_and_split(
        text_splitter=text_splitter
    )

    for doc in docs:
        print(doc.page_content)
        print("\n")