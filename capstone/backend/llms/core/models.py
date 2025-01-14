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

# TODO: Make more function.
@dataclass
class ChatModel:

     # TODO: add more parameter
    model: str = 'llama3.2'
    """ Declare model 
    Default: llama3.2
    
    """

    top_k: Optional[int] = None
    """ top_k parameter """
    top_p: Optional[int] = None
    """ top_p parameter """
    prompt_template : Optional[str] = None
    
    def __post_init__(self) -> None:
        print(f"Loading.. {self.model}")
        self.llm = OllamaLLM(model=self.model)
        print(f"Using {self.model} now.")
    

    # TODO: Make more reriable
    def query(self, question: str) -> str:
        """ Normal chat with AI

        Args:
            question (str): Prompt for chat

        Returns:
            str: Answer from LLM model.
        """
        return self.llm.invoke(question)
    

    # TODO: Make more reriable
    def query_with_template(self, prompt_template: str) -> str:
        """ Query with prompttemplate

        Args:
            prompt_template (str): Prompt template that you need to use.

        Returns:
            str: Answer from LLM model. 
        """
        chain = prompt_template | self.llm
        return chain.invoke("Hello")

if __name__ == '__main__':

    prompt_template = "Tell me a {adjective} joke"
    prompt = PromptTemplate(
        input_variables=["adjective"], template=prompt_template
    )

    test = ChatModel(model='llama3.2')
    print(test.query("Can you sending me some mr beast channel"))
    print(test.query_with_template(prompt))
