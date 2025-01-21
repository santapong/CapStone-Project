from langchain_core.prompts import (
    PromptTemplate,
    SystemMessagePromptTemplate, 
    HumanMessagePromptTemplate
    )

# Zero shot prompt template.
zero_shot_input_variable = []
zero_shot_prompt_template ="""

"""

# Few show prompt template.
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
