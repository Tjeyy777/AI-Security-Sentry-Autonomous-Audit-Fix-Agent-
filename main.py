import os
from agent.graph import app

if __name__ == "__main__":
    print("🚀 Security Agent Start")
    
    initial_state = {
        "repo_path": "vulnerable.py",
        "scan_plan": [], 
        "findings": [],
        "emergency": False,
        "summary": "",
        "status": "Starting"
    }

    result = app.invoke(initial_state)

    print("\n=== 🛡️  AUDIT RESULTS ===")
    for tool in result.get("findings", []):
        print(f"\n[{tool['tool'].upper()}] - Found {len(tool['issues'])} issues")
        for issue in tool['issues']:
            print(f"  - {issue}")
    
    print("\n=== 🧠 AI SUMMARY ===")
    print(result.get("summary"))
    
    # main.py execution
print("🚀 Security Agent Start")
result = app.invoke(initial_state)

# --- Save Phase 4 Output ---
with open("SECURITY_AUDIT.md", "w", encoding="utf-8") as f:
    f.write(result["summary"])

print("\n✨ Phase 4 Complete: Report saved to SECURITY_AUDIT.md")