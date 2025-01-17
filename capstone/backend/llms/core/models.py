# import library and module
import os 
import logging

from typing import Optional

from dataclasses import dataclass
from dotenv import load_dotenv

from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from capstone.backend.llms.prompt_teamplate.prompt_template import *

logging.getLogger(__name__)

logging.warning(f"This {__name__} file will be change in future.")

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