from langchain_chroma import Chroma
from config.llm import get_embeddings
import os

PERSIST_DIRECTORY = "data/chroma"


# -------------------------
# Document Vector Store
# -------------------------

def get_vector_store(collection_name="research_papers"):
    embeddings = get_embeddings()

    if os.getenv("CHROMA_HOST"):
        import chromadb
        client = chromadb.HttpClient(host=os.getenv("CHROMA_HOST"), port=int(os.getenv("CHROMA_PORT", 8000)))
        return Chroma(client=client, collection_name=collection_name, embedding_function=embeddings)
    else:
        return Chroma(
            collection_name=collection_name,
            embedding_function=embeddings,
            persist_directory=PERSIST_DIRECTORY,
        )


def add_chunks_to_vector_store(chunks, metadata=None):
    vector_store = get_vector_store()

    metadatas = []
    for i, chunk in enumerate(chunks):
        meta = {"chunk_id": i}
        if metadata:
            meta.update(metadata)
        metadatas.append(meta)

    vector_store.add_texts(texts=chunks, metadatas=metadatas)


def retrieve_relevant_chunks(query: str, k: int = 3):
    vector_store = get_vector_store()

    results = vector_store.similarity_search(query, k=k)

    return [doc.page_content for doc in results]


# -------------------------
# Conversation Memory Store
# -------------------------

def get_memory_store(collection_name="conversation_memory"):
    embeddings = get_embeddings()

    if os.getenv("CHROMA_HOST"):
        import chromadb
        client = chromadb.HttpClient(host=os.getenv("CHROMA_HOST"), port=int(os.getenv("CHROMA_PORT", 8000)))
        return Chroma(client=client, collection_name=collection_name, embedding_function=embeddings)
    else:
        return Chroma(
            collection_name=collection_name,
            embedding_function=embeddings,
            persist_directory=PERSIST_DIRECTORY,
        )


def save_conversation(session_id: str, question: str, answer: str):
    memory_store = get_memory_store()

    text = f"User: {question}\nAssistant: {answer}"

    memory_store.add_texts(
        texts=[text],
        metadatas=[{"session_id": session_id}]
    )


def retrieve_session_memory(session_id: str, query: str, k: int = 3):
    memory_store = get_memory_store()

    results = memory_store.similarity_search(
        query,
        k=k,
        filter={"session_id": session_id}
    )

    return [doc.page_content for doc in results]

def save_summary(session_id: str, summary: str):
    memory_store = get_memory_store()

    memory_store.add_texts(
        texts=[f"Summary: {summary}"],
        metadatas=[{"session_id": session_id, "type": "summary"}]
    )
