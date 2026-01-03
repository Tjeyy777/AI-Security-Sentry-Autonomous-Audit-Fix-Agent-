
# 🛡️ AI Security Sentry
### Autonomous Audit & Fix Agent

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)


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
# 🛡️ AI Security Sentry: User Guide

Welcome to the **AI Security Sentry**! This tool is an autonomous security engineer designed to find, analyze, and help fix vulnerabilities in Python projects. It uses **LangGraph** for decision-making and **GPT-4o** as the "brain" to understand code context.



---

## 🛠️ 1. Local Installation
Before you can run the agent, you need to prepare your environment.

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/Tjeyy777/AI-Security-Sentry-Autonomous-Audit-Fix-Agent-.git](https://github.com/Tjeyy777/AI-Security-Sentry-Autonomous-Audit-Fix-Agent-.git)
   cd AI-Security-Sentry

2.Create a Virtual Environment:
# Windows
```python -m venv venv
venv\Scripts\activate
```
# Mac/Linux
```python3 -m venv venv
source venv/bin/activate
```
# 3.Install Dependencies:

``` pip install -r requirements.txt ```

# 4.Set up OpenAI API Key: Create a file named .env in the root folder and add:
```OPENAI_API_KEY=your_actual_key_here```


# 🚀 2. How to Use (Local Modes)
Run the agent using the command: python main.py. You will be presented with a menu:

### 📂 Option 1: Project Scan (Professional Mode)

This mode is built for real-world development. It allows the agent to leave the sandbox and audit any external project folder on your machine.

* **What it does:** Recursively crawls an entire external folder, identifying all Python files for analysis.
* **How to use:** When prompted, paste the **full directory path** of the project you want to audit.
    * *Example:* `C:/Users/YourName/Desktop/MyWebProject`
* **Outcome:** 1.  The agent runs a full security sweep using **Semgrep** and **TruffleHog**.
    2.  The AI Auditor analyzes the findings for context.
    3.  A comprehensive report named `SECURITY_AUDIT.md` is generated and saved **directly inside** the target project folder for easy access.

### 🧪 Option 2: Sandbox Test (Demo Mode)

Perfect for first-time users or for demonstrating the agent's capabilities without risking changes to a live project.

* **What it does:** Instantly targets the built-in `vulnerable.py` file included in this repository. 
* **How to use:** Select **Option 2** from the main menu. No path input is required.
* **Outcome:** * The agent performs a "deep dive" scan on the sample file.
    * You can watch the **Auditor Node** explain exactly why the sample code is insecure.
    * Ideal for verifying that your API keys and environment are set up correctly.

---

## 🤖 3. The Multi-Agent Architecture

The **AI Security Sentry** is not a simple script; it is a sophisticated **Directed Acyclic Graph (DAG)** built on **LangGraph**. When you initiate a scan, the agent orchestrates the workflow through four specialized nodes:

### 🗺️ Node 1: The Planner
* **Role:** The Strategist.
* **Logic:** It maps out the target directory, filters out irrelevant files (like those in `.gitignore` or `venv`), and builds a prioritized queue of Python files to be analyzed.

### 🔍 Node 2: The Scanner
* **Role:** The Investigator.
* **Tools:** Runs a dual-engine scan:
    * **Semgrep:** Performs Static Analysis (SAST) to find logic flaws like SQL injection or insecure imports.
    * **TruffleHog:** Scours the code for hardcoded secrets, API keys, and private tokens.

### 🧠 Node 3: The Auditor (AI Engine)
* **Role:** The Expert Analyst (Powered by GPT-4o).
* **Intelligence:** It reviews raw data from the Scanner. The Auditor is trained to:
    * **Eliminate False Positives:** Contextually understands if a "bug" is actually intended.
    * **Risk Scoring:** Assigns severity levels (Critical, High, Medium, Low).
    * **Plain English Explanations:** Translates complex security vulnerabilities into readable summaries.

### 🛠️ Node 4: The Fixer
* **Role:** The Security Engineer.
* **Action:** Automatically generates secure code patches. 
    * **Safety Gate:** In Local Mode, the Fixer will **always ask for user permission** before modifying any source code.
    * **CI/CD Mode:** Generates a "Proposed Fixes" report without altering the build files.

---

☁️ 4. Automating with GitHub Actions
To make the agent scan your code automatically every time you git push, follow these steps in your repository:

Step A: Add your Secret
Go to Settings > Secrets and variables > Actions and add:
Name: OPENAI_API_KEY
Value: (Your OpenAI Key)

Step B: Create the Workflow
Create a file at .github/workflows/security.yml and paste:
name: AI Security Sentry

on: [push]
```YAML
jobs:
  scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.10'
      - name: Run Agent
        env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          GITHUB_ACTIONS: "true"
        run: |
          pip install -r requirements.txt
          python main.py .
      - name: Save Report
        uses: actions/upload-artifact@v4
        with:
          name: security-report
          path: SECURITY_AUDIT.md  
```
## 📊 5. Understanding the Report

Every scan generates a comprehensive `SECURITY_AUDIT.md` file. The agent uses a standardized risk-rating system to help you prioritize your security backlog.

### 🛑 Severity Levels

| Severity | Risk Level | Description | Example |
| :--- | :--- | :--- | :--- |
| 🔴 **Critical** | **Immediate** | Direct exploits that could lead to data breaches. | SQL Injection, Remote Code Execution |
| 🟠 **High** | **Serious** | Significant flaws that compromise security posture. | Broken Authentication, Leaked API Keys |
| 🟡 **Medium** | **Best Practice** | Deviations from security standards and hardening. | Hardcoded Configs, Insecure Imports |

### 📝 What's Inside Each Finding?

The AI Auditor doesn't just list errors; it provides a full engineering context for every discovery:

* **📍 Exact Location:** Clearly identifies the file path and specific line number where the issue resides.
* **⚠️ The "Danger" Analysis:** A detailed explanation from the AI on *why* this specific line is a threat and how an attacker might exploit it.
* **✅ Remediation Snippet:** A "copy-paste ready" code block showing the secure version of your code.
* **🔗 References:** Links to CWE (Common Weakness Enumeration) or OWASP standards when applicable.

---

💡 Pro-Tip for Users
If you are running this on a large project, make sure to add folders like tests/ or dist/ to your .gitignore so the agent focuses only on your main source code!

