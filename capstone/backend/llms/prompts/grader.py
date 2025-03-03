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

### Grading Criteria:  
1. If the document **contains information that can be used to answer the question**, grade it as relevant.  
2. Consider synonyms, paraphrased content, and implicit meanings, not just exact keyword matches.  
3. If the document **lacks sufficient information** or is **completely unrelated**, grade it as not relevant.  

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