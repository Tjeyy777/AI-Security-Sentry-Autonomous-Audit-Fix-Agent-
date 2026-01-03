import sys
import os
from agent.graph import app

def show_menu():
    print("\n" + "="*40)
    print("🛡️  WELCOME TO AI SECURITY SENTRY  🛡️")
    print("="*40)
    print("1. 📂 Scan a Project (Enter a folder path)")
    print("2. 🧪 Run Sandbox Test (Scan 'vulnerable.py')")
    print("3. ❌ Exit")
    print("="*40)

def run_agent():
    show_menu()
    choice = input("Select an option (1-3): ").strip()

    if choice == '1':
        target_path = input("📂 Enter the full path to your project folder: ").strip()
        if not os.path.exists(target_path):
            print(f"❌ Error: Path '{target_path}' not found.")
            return
    elif choice == '2':
        target_path = "vulnerable.py"
        if not os.path.exists(target_path):
            print("❌ Error: 'vulnerable.py' not found in this folder.")
            return
        print("🧪 Running Sandbox Test on 'vulnerable.py'...")
    elif choice == '3':
        print("Goodbye! 👋")
        return
    else:
        print("⚠️ Invalid choice. Exiting.")
        return

    # --- Setup Initial State ---
    initial_state = {
        "repo_path": target_path,
        "scan_plan": [], 
        "findings": [],
        "emergency": False,
        "summary": "",
        "status": "Starting"
    }

    print(f"\n🚀 Security Agent Start: Processing {target_path}...")
    
    # --- Invoke the LangGraph Brain ---
    result = app.invoke(initial_state)

    # --- Save the Report ---
    # If it's a folder, save inside it. If it's a file, save in the current dir.
    if os.path.isdir(target_path):
        report_path = os.path.join(target_path, "SECURITY_AUDIT.md")
    else:
        report_path = "SECURITY_AUDIT.md"

    with open(report_path, "w", encoding="utf-8") as f:
        f.write(result.get("summary", "No summary generated."))

    print(f"\n✨ Audit Complete!")
    print(f"📊 Report saved to: {os.path.abspath(report_path)}")

if __name__ == "__main__":
    run_agent()