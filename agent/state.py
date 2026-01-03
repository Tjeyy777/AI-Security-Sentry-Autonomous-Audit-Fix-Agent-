from typing import TypedDict, List, Dict, Any

class AgentState(TypedDict):
    repo_path: str
    scan_plan: List[str]     # List of tools to run: ["semgrep", "trufflehog"]
    findings: List[Dict]      # Structured results from tools
    summary: str             # Final LLM output
    emergency: bool          # True if secrets are found
    status: str