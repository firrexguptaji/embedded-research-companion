from config.llm import get_llm

llm = get_llm()


def planner(state):
    prompt = f"""
You are a research planner.

Create a short reasoning plan to answer:

Question: {state['question']}
"""
    response = llm.invoke(prompt)
    return {"plan": response.content}
