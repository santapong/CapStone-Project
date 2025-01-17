import logging
from dotenv import load_dotenv

load_dotenv()

from pydantic import BaseModel # Provide pydantics 
from dataclasses import dataclass
from typing import Optional, Union, List

from langchain_community.document_loaders import WebBaseLoader


# TODO: Add Logging for Production Env
# Choice from >>  Built-in Log or Loguru

# TODO: Implement to use with dataclass or pydantic model.
class WebLoaderManager:

    # Make it can import multiple website.  
    # see: https://python.langchain.com/docs/integrations/document_loaders/web_base/#initialization-with-multiple-pages
    def __init__(self, URL: Union[List, str]  ):
        print(f"Loading.. {URL}")
        self.loader = WebBaseLoader(URL)
        
    def get_URL(self)-> List:
        """
        To get Document from URL

        Returns:
            List: Document of website content
        """
        self.docs = self.loader.load()
        return self.docs


if __name__ == '__main__':

    URL = ["https://www.example.com/", "https://google.com"]

    test = WebLoaderManager(URL)

    print(test.get_URL())