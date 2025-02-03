from langchain_core.prompts import (
    PromptTemplate,
    SystemMessagePromptTemplate, 
    HumanMessagePromptTemplate,
    ChatPromptTemplate
    )



# TODO: Make it must more good answer.
# rlm/rag-prompt
# see https://smith.langchain.com/hub/rlm/rag-prompt?organizationId=2ee7223e-2f84-4a9b-924e-232565e6e92c
RAG_prompt_template = """

                You are an assistant for question-answering tasks. Use the following pieces of 
                retrieved context to answer the question. If you don't know the answer, just say 
                that you don't know. Use three sentences maximum and keep the answer concise.    


                Context: {context} 
                Answer:
                """
# Question: {question} 


# RAG Prompt template
prompt = ChatPromptTemplate(
    ("human",RAG_prompt_template),
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
     anser = "test"
     with open("anwser.txt",'a') as f:
        f.write(anser)