from langgraph.graph import StateGraph, END
from .state import AgentState
from .nodes.planner import planner_node
from .nodes.scanner import scanner_node
from .nodes.auditor import auditor_node
from .nodes.fixer import fixer_node  # <-- 1. Import the fixer

def build_graph():
    graph = StateGraph(AgentState)

    # 2. Add the nodes to the graph
    graph.add_node("planner", planner_node)
    graph.add_node("scanner", scanner_node)
    graph.add_node("auditor", auditor_node)
    graph.add_node("fixer", fixer_node)    # <-- 3. Add fixer node

    # 4. Define the updated flow
    graph.set_entry_point("planner")
    graph.add_edge("planner", "scanner")
    graph.add_edge("scanner", "auditor")
    graph.add_edge("auditor", "fixer")      # <-- 5. Auditor now goes to Fixer
    graph.add_edge("fixer", END)            # <-- 6. Fixer is now the final step

    return graph.compile()

app = build_graph()