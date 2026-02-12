from app.memory.vector_store import retrieve_relevant_chunks
from app.state import ResearchState


def document_agent(state: ResearchState):
    chunks = retrieve_relevant_chunks(state["question"], k=3)
    return {"document_context": chunks}
