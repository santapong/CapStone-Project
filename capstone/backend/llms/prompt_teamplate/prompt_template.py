from langchain_core.prompts import (PromptTemplate, 
                                    SystemMessagePromptTemplate, 
                                    HumanMessagePromptTemplate)
from langchain_ollama import OllamaLLM

# Few show prompt template to make model can learn.
few_shot_input_variable = ["name"]
few_shot_prompt_template = """

Your name is {name}.

"""

# Test prompt for evaluation of model.
test_prompt_input_variable = []
test_prompt_template = """

"""

if __name__ == '__main__':
    prompt_template=PromptTemplate(
        input_variables=few_shot_input_variable,
        template=few_shot_prompt_template
    )

    llms = OllamaLLM(model='llama3.2')
    chains = prompt_template | llms

    print(chains.invoke("Hello"))    