import os
import json

from pprint import pprint
from typing import List
from dotenv import load_dotenv

from langchain_core.tools import Tool
from langchain_community.document_loaders import WebBaseLoader
from langchain_google_community import GoogleSearchAPIWrapper

from dotenv import load_dotenv
from langchain_google_community import GoogleSearchAPIWrapper
from langchain_core.tools import Tool

load_dotenv()

def google_search(
    query, 
    top_k: int=10
    ):
    wrapper = GoogleSearchAPIWrapper(
        google_cse_id=os.getenv("GOOGLE_CSE_ID"),
        google_api_key=os.getenv("GOOGLE_API_KEY"),
    )
    
    result = lambda query, top_k: list(wrapper.results(query=query, num_results=top_k))

    links = [
        result["link"] for result in result(query=query, top_k=top_k) 
    ]
    
    documents = WebBaseLoader(web_paths=links).load()
    pprint(documents)    
    
data = google_search(query="Test")