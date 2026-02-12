from app.memory.vector_store import retrieve_session_memory


def memory_agent(state):
    memory = retrieve_session_memory("global_session", state["question"], k=2)
    return {"memory_context": memory}
