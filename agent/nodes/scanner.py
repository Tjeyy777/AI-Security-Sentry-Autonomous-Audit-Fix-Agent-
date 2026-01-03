from agent.state import AgentState
from tools.semgrep import run_semgrep
from tools.trufflehog import run_trufflehog

def scanner_node(state: AgentState) -> AgentState:
    print("\n--- 🛠️  EXECUTING SCANS ---")
    findings = []
    
    for tool in state.get("scan_plan", []):
        if tool == "semgrep":
            findings.append(run_semgrep(state["repo_path"]))
        elif tool == "trufflehog":
            findings.append(run_trufflehog(state["repo_path"]))

    emergency = any(f["tool"] == "trufflehog" and len(f["issues"]) > 0 for f in findings)

    return {
        **state,
        "findings": findings,
        "emergency": emergency,
        "status": "Scanning complete"
    }