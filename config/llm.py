from langchain_ollama import ChatOllama
from langchain_ollama import OllamaEmbeddings


def get_llm():
    return ChatOllama(
        model="mistral",
        temperature=0.2
    )


def get_embeddings():
    return OllamaEmbeddings(
        model="nomic-embed-text"
    )
