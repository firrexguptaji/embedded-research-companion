from app.graph.graph import build_graph


class ResearchEngine:

    def __init__(self):
        self.graph = build_graph()

    def run(self, question: str):
        state = {
            "question": question,
            "plan": "",
            "route": [],
            "document_context": [],
            "wiki_context": [],
            "memory_context": [],
            "final_answer": "",
        }

        result = self.graph.invoke(state)

        return result["final_answer"]
