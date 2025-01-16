import os 
import logging

from dotenv import load_dotenv
from abc import abstractmethod, ABC

from capstone.backend.llms.core.models import ChatModel
from capstone.backend.llms.vectordb.session import VectorDBConnect

from capstone.backend.llms.prompt_teamplate.prompt_template import (few_shot_prompt_template,
                                                                    few_shot_input_variable,
                                                                    test_prompt_template,
                                                                    test_prompt_input_variable)

from capstone.backend.llms.utils.splitter import SplitterManager

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

## Define Class for Retrieval-Augmented Generation ( RAG. )
class baseRAG(ABC):
    pass

## Load Document
# Using LoaderManger to Handle PDF, Website, Text, API Upload.
    def load(self):
        pass
        
## Split text


## Embedding


## Stored VectorDB & Retreieval


## LLMs


## Generation


## Performance Zone


## Evaluation

if __name__ == '__main__':

    test = baseRAG()