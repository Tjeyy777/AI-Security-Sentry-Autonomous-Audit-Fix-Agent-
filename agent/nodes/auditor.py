import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from agent.state import AgentState

load_dotenv()

def auditor_node(state: AgentState) -> AgentState:
    print("--- 🧠 AI AUDITOR: MAPPING SUGGESTED CHANGES ---")
    findings = state.get("findings", [])
    
    # Get the code for the AI to analyze line-by-line
    vulnerable_file_path = "vulnerable.py"
    code_content = ""
    if os.path.exists(vulnerable_file_path):
        with open(vulnerable_file_path, "r") as f:
            code_content = f.read()

    llm = ChatOpenAI(model="gpt-4o", temperature=0)
    
    # We explicitly ask for a "Diff" style explanation
    prompt = f"""
    You are a Senior Security Engineer. Review the following code and scanner findings.
    
    SOURCE CODE:
    {code_content}

    SCANNER FINDINGS:
    {findings}
    
    TASK:
    Generate a report in Markdown. For every vulnerability, you MUST provide:
    1. The Vulnerability Name (with a 🔴, 🟠, or 🟡 based on severity).
    2. The exact Line Number.
    3. A 'Suggested Change' section showing:
       - **❌ Original:** (The dangerous line)
       - **✅ Recommended:** (The secure replacement)

    Format the report to be clean and professional for a GitHub Pull Request comment.
    """
    
    try:
        response = llm.invoke(prompt)
        summary = response.content
    except Exception as e:
        summary = f"AI Audit failed: {str(e)}."

    return {**state, "summary": summary}