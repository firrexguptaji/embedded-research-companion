from config.llm import get_llm

llm = get_llm()


def router(state):
    prompt = f"""
Based on this plan, choose which agents to use.

Available:
- document
- wikipedia
- memory

Return comma-separated list.

Plan:
{state['plan']}
"""
    response = llm.invoke(prompt)
    raw = response.content.lower()

    selected = []
    for agent in ["document", "wikipedia", "memory"]:
        if agent in raw:
            selected.append(agent)

    if not selected:
        selected = ["document"]

    return {"route": selected}
