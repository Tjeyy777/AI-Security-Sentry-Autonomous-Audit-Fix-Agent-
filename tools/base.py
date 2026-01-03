from typing import List, Dict, TypedDict

class ToolResult(TypedDict):
    tool: str
    issues: List[Dict]

def standard_result(tool: str, issues: List[Dict]) -> ToolResult:
    return {"tool": tool, "issues": issues}