from langchain_core.prompts import ( 
    PromptTemplate,
    ChatPromptTemplate,
    )

# Grader Prompt
system = """
You are a grader assessing the relevance of a retrieved document to a user question.  

- Here is the retrieved document:  

  {context}  

- Here is the user question:  

  {question}  

Grading Criteria:
1.The document is relevant if it contains information that can be used to answer the question, even if paraphrased, implicit, or using synonyms.
2.Language Differences: If the document is in a different language than the question, assess its relevance based on translation rather than exact wording.
3.The document is not relevant if it lacks sufficient information or is completely unrelated to the question.

### Output Format:  
Respond only in JSON format with one of the following:  
- If relevant: {{"binary_score":"yes"}}
- If not relevant: {{"binary_score":"no"}}  

**Example Response:**  
```json
{{"binary_score":"yes"}}

"""

decision_prompt = ChatPromptTemplate.from_messages(
    [("system",system)]
)