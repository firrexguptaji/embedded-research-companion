import wikipedia


def wiki_agent(state):
    try:
        summary = wikipedia.summary(state["question"], sentences=3)
        return {"wiki_context": [summary]}
    except Exception:
        return {"wiki_context": []}
