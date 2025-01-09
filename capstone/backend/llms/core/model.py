# import library and module
import os 
import logging

from typing import Optional

from dataclasses import dataclass
from dotenv import load_dotenv

from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from capstone.backend.llms.utils.prompt_template import *

# Load config from .env file
load_dotenv()

# TODO: Thing more about it
@dataclass
class ChatModel:

     # TODO: add more parameter
    model: str
    """ Declare model """

    top_k: Optional[int] = None
    """ top_k parameter """
    top_p: Optional[int] = None
    """ top_p parameter """
    prompt_template : Optional[str] = None
    
    def __post_init__(self) -> None:
        self.llm = OllamaLLM(model=self.model)
        print(f"Using {self.model} now.")
    

    # TODO: Make more reriable
    def query(self, question: str) -> str:
        """ Normal chat with AI

        Args:
            question (str): _description_

        Returns:
            str: _description_
        """
        return self.llm.invoke(question)
    

    # TODO: Make more reriable
    def query_with_template(self, prompt_template: str):
        """ Query with prompttemplate

        Args:
            prompt_template (str): _description_

        Returns:
            _type_: _description_
        """
        chain = prompt_template | self.llm
        return chain.invoke("Hello")

if __name__ == '__main__':

    prompt_template = "Tell me a {adjective} joke"
    prompt = PromptTemplate(
        input_variables=["adjective"], template=prompt_template
    )

    test = ChatModel(model='llama3.2')
    print(test.query("Hello"))
    print(test.query_with_template(prompt))
