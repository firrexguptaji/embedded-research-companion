from langgraph.graph import StateGraph, END
from app.state import ResearchState

from app.agents.planner import planner
from app.agents.router import router
from app.agents.document_agent import document_agent
from app.agents.wiki_agent import wiki_agent
from app.agents.memory_agent import memory_agent
from app.agents.aggregator import aggregator


def route_decision(state: ResearchState):
    """
    Dynamically route to selected agents.
    """
    return state["route"]


def build_graph():
    graph = StateGraph(ResearchState)

    # Add nodes
    graph.add_node("planner", planner)
    graph.add_node("router", router)
    graph.add_node("document", document_agent)
    graph.add_node("wikipedia", wiki_agent)
    graph.add_node("memory", memory_agent)
    graph.add_node("aggregator", aggregator)

    # Entry point
    graph.set_entry_point("planner")

    # Basic flow
    graph.add_edge("planner", "router")

    # Conditional routing
    graph.add_conditional_edges(
        "router",
        route_decision,
        {
            "document": "document",
            "wikipedia": "wikipedia",
            "memory": "memory",
        },
    )

    # All selected agents go to aggregator
    graph.add_edge("document", "aggregator")
    graph.add_edge("wikipedia", "aggregator")
    graph.add_edge("memory", "aggregator")

    graph.add_edge("aggregator", END)

    return graph.compile()
