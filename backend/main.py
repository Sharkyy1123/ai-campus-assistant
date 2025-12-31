from llm import llm_predict
from rag import ask_rag

def agent_answer(query: str):
    context = ask_rag(query)

    prompt = f"""
    Context:
    {context}

    Question:
    {query}
    """

    return llm_predict(prompt)
