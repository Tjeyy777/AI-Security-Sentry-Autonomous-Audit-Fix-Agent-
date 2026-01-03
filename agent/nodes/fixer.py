import os
from langchain_openai import ChatOpenAI
from agent.state import AgentState

def fixer_node(state: AgentState) -> AgentState:
    is_github = os.getenv("GITHUB_ACTIONS") == "true"
    
    if is_github:
        print("🤖 Running in CI: Skipping interactive fix for safety.")
        return state
    print("\n--- ✋ HUMAN-IN-THE-LOOP: APPROVAL REQUIRED ---")
    
    # Ask the user for permission
    confirm = input("🧪 AI has generated security patches. Apply changes to vulnerable.py? (y/n): ")
    
    if confirm.lower() != 'y':
        print("🚫 Fixes rejected by user. Skipping repair phase.")
        return state

    print("--- 🛠️  AI FIXER: APPLYING PATCHES ---")
    target_file = "vulnerable.py"
    
    with open(target_file, "r") as f:
        original_code = f.read()

    llm = ChatOpenAI(model="gpt-4o", temperature=0)
    
    # We ask the LLM to perform the actual refactor based on its own previous audit
    prompt = f"""
    You are an Automated Security Refactoring Tool.
    
    SECURITY AUDIT REPORT:
    {state['summary']}
    
    ORIGINAL CODE:
    {original_code}
    
    TASK:
    Rewrite the file '{target_file}' to fix all vulnerabilities identified in the report.
    - Maintain all original logic and functionality.
    - Return ONLY the raw Python code. Do not include markdown backticks or explanations.
    """
    
    try:
        fixed_code = llm.invoke(prompt).content.strip()
        
        # Clean up any accidental markdown formatting
        if fixed_code.startswith("```"):
            fixed_code = "\n".join(fixed_code.split("\n")[1:-1])

        with open(target_file, "w", encoding="utf-8") as f:
            f.write(fixed_code)
            
        print(f"✅ SUCCESS: {target_file} has been secured and updated.")
    except Exception as e:
        print(f"❌ Error applying fixes: {e}")

    return state