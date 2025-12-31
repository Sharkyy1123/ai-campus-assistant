from llm import llm_predict
from rag import ask_rag
from memory import memory

def agent_answer(query: str):
    context = ask_rag(query)

    prompt = f"""
    Context:
    {context}

    Question:
    {query}
    """

    response = llm_predict(prompt)

    # store conversation
    memory.add(query, response)

    return response
