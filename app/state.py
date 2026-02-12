from typing import TypedDict, List, Dict, Any


class ResearchState(TypedDict):
    question: str
    plan: str
    route: List[str]
    document_context: List[str]
    wiki_context: List[str]
    memory_context: List[str]
    final_answer: str
