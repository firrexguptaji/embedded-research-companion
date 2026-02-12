from config.llm import get_llm

llm = get_llm()


def aggregator(state):
    context = "\n\n".join(
        state.get("document_context", [])
        + state.get("wiki_context", [])
        + state.get("memory_context", [])
    )

    prompt = f"""
You are an advanced research assistant.

Use the context below to answer clearly.

Context:
{context}

Question:
{state['question']}

Answer:
"""
    response = llm.invoke(prompt)

    return {"final_answer": response.content}
