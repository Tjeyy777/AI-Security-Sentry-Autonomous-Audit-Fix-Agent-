from agent.state import AgentState

def planner_node(state: AgentState) -> AgentState:
    print("--- 🧠 PLANNING SCAN ---")
    # For now, we hardcode the tools. 
    # Later, you can let an LLM decide based on the file types!
    return {
        **state,
        "scan_plan": ["semgrep", "trufflehog"],
        "status": "Plan created"
    }