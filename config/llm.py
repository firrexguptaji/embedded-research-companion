from langchain_ollama import ChatOllama, OllamaEmbeddings

OLLAMA_BASE_URL = "http://ollama:11434"



def get_llm():
    return ChatOllama(
        model="mistral",
        base_url=OLLAMA_BASE_URL,
        temperature=0.2
    )


def get_embeddings():
    return OllamaEmbeddings(
        model="nomic-embed-text",
        base_url=OLLAMA_BASE_URL
    )
