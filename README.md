Markdown

# 🛡️ AI Security Sentry
### Autonomous Audit & Fix Agent

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

**AI Security Sentry** is an intelligent, agentic security engineer that lives in your CLI and CI/CD pipeline. Unlike traditional scanners that simply dump a list of warnings, this agent **reasons** about vulnerabilities, filters false positives, and **automatically writes fixes** for your code.

Built on **LangGraph**, **OpenAI GPT-4o**, and industry-standard tools (**Semgrep**, **TruffleHog**), it acts as a proactive security teammate that stops bugs before they merge.

---

## 🧠 The Architecture

This is not just a script; it is a **Multi-Agent System**. The workflow is orchestrated by a state graph that passes information between specialized nodes.



### The Agents
1.  **🗺️ The Planner:**
    * **Role:** The Strategist.
    * **Task:** Scans the directory tree, identifies relevant source code, and ignores noise (like `venv` or `.git`).
2.  **👀 The Scanner (Truth Layer):**
    * **Role:** The Investigator.
    * **Task:** Runs deterministic tools (**Semgrep** for SAST, **TruffleHog** for secrets) to gather raw evidence.
3.  **🧠 The Auditor (Intelligence Layer):**
    * **Role:** The Analyst.
    * **Task:** Reviews raw findings against the actual source code. It filters false positives, calculates risk scores, and generates a structured **Markdown Report**.
4.  **🛠️ The Fixer (Action Layer):**
    * **Role:** The Engineer.
    * **Task:** Generates secure code patches.
    * **Safety:** Includes a **Human-in-the-Loop** gate—it will never modify your code without explicit permission (CLI) or configuration (CI/CD).

---

## 🚀 Key Features

-   **Hybrid Detection:** Combines the speed of static analysis with the reasoning of Large Language Models.
-   **Secret Detection:** actively hunts for hardcoded API keys, passwords, and tokens.
-   **Context-Aware Fixes:** The AI understands *why* a line is dangerous and suggests a fix that maintains original logic (e.g., swapping `pickle` for `json`, or adding `subprocess.run(check=True)`).
-   **CI/CD Native:** Runs automatically on GitHub Actions to block vulnerable commits.
-   **Professional Reporting:** Generates an investor-ready `SECURITY_AUDIT.md` with every run.

---

## 🛠️ Installation & Setup

### Prerequisites
-   Python 3.10 or higher
-   Git
-   An OpenAI API Key

### 1. Clone the Repository
```bash
git clone [https://github.com/Tjeyy777/AI-Security-Sentry-Autonomous-Audit-Fix-Agent-.git](https://github.com/Tjeyy777/AI-Security-Sentry-Autonomous-Audit-Fix-Agent-.git)
cd AI-Security-Sentry


2. Create a Virtual Environment
Windows:
Bash
python -m venv venv
source venv/Scripts/activate

Mac/Linux:
Bash
python3 -m venv venv
source venv/bin/activate

3. Install Dependencies
Bash
pip install -r requirements.txt
This installs LangChain, LangGraph, Semgrep, and other core libraries.

4. Configure Environment
Create a .env file in the root directory and add your OpenAI API key:
Code snippet
OPENAI_API_KEY=sk-proj-12345...

💻 Usage
Local Mode (CLI)
Run the agent manually to scan your current project folder.

Bash
python main.py
What happens next?

Plan: The agent lists files to scan.
Scan: Semgrep and TruffleHog run in the background.
Audit: The AI analyzes findings and creates SECURITY_AUDIT.md.
Fix (Optional): The agent will pause and ask:

🧪 AI has generated security patches. Apply changes? (y/n)
Type y: The agent rewrites the vulnerable files with secure code.
Type n: The agent exits, leaving the report for you to review.

CI/CD Mode (GitHub Actions)
This agent is pre-configured to run on every git push.
Navigate to the Actions tab in your repository.
Ensure you have added OPENAI_API_KEY to your Repository Secrets.

On every push, the agent will:
Scan the code.
Generate a report.
Upload SECURITY_AUDIT.md as a build artifact.

📊 Example Output
The agent generates a professional Security Audit Report (SECURITY_AUDIT.md):

🔴 SQL Injection Detected
Location: vulnerable.py:25

❌ Original Code:

Python
cursor.execute("SELECT * FROM users WHERE name = '" + user_input + "'")
✅ Recommended Fix:

Python
cursor.execute("SELECT * FROM users WHERE name = ?", (user_input,))
Reason: Parameterized queries prevent attackers from injecting malicious SQL commands.

🤝 Contributing
Contributions are welcome! Please open an issue or submit a Pull Request.

Fork the Project.
Create your Feature Branch (git checkout -b feature/AmazingFeature).
Commit your Changes (git commit -m 'Add some AmazingFeature').
Push to the Branch (git push origin feature/AmazingFeature).
Open a Pull Request.
