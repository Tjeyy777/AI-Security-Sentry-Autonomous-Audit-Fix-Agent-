import json
import subprocess
import os
from tools.base import standard_result

def run_semgrep(repo_path: str):
    rel_path = os.path.relpath(repo_path)
    # Get path to the local rules.yaml we just created
    rules_path = os.path.join(os.getcwd(), "rules.yaml")
    
    print(f"🔍 [Semgrep] Local Rule Scan: {rel_path}")
    
    env = os.environ.copy()
    env["PYTHONUTF8"] = "1"
    
    # We point --config directly to our local file
    cmd = [
        "semgrep", "scan", 
        f"--config={rules_path}", 
        "--json", 
        "--no-git-ignore", 
        rel_path
    ]

    try:
        result = subprocess.run(
            cmd, 
            capture_output=True, 
            text=True, 
            shell=True,
            env=env,
            encoding='utf-8', 
            errors='ignore'
        )
        
        output = result.stdout.strip()
        # Find the JSON block
        start_index = output.find('{')
        if start_index == -1:
            return standard_result("semgrep", [])

        data = json.loads(output[start_index:])
        issues = []
        for finding in data.get("results", []):
            issues.append({
                "rule_id": finding["check_id"],
                "file": finding["path"],
                "line": finding["start"]["line"],
                "message": finding["extra"]["message"],
                "severity": finding["extra"].get("severity", "UNKNOWN")
            })
            
        print(f"✅ Semgrep Finished: Found {len(issues)} issues.")
        return standard_result("semgrep", issues)
    except Exception as e:
        print(f"❌ Semgrep Error: {e}")
        return standard_result("semgrep", [])