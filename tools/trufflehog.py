import json
import subprocess
import os
from .base import standard_result

def run_trufflehog(repo_path: str):
    # Locate the local exe in your root folder
    truffle_exe = os.path.join(os.getcwd(), "trufflehog.exe")
    print(f"🐷 [TruffleHog] Scanning: {repo_path}")
    
    # --no-update: Prevents Windows file-locking crashes
    # --exclude-paths=venv: Stops scanning the library folder (IMPORTANT)
    cmd = [
        truffle_exe, 
        "filesystem", 
        repo_path, 
        "--json", 
        "--no-update", 
        "--exclude-paths=venv",
        "--only-verified=false"
    ]

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            shell=True,
            encoding='utf-8',
            errors='ignore'
        )

        issues = []
        for line in result.stdout.splitlines():
            if not line.strip(): continue
            try:
                finding = json.loads(line)
                issues.append({
                    "file": finding.get("SourceMetadata", {}).get("Data", {}).get("Filesystem", {}).get("file"),
                    "line": finding.get("SourceMetadata", {}).get("Data", {}).get("Filesystem", {}).get("line"),
                    "secret_type": finding.get("DetectorName"),
                    "verified": finding.get("Verified", False)
                })
            except: continue

        return standard_result("trufflehog", issues)
    except Exception as e:
        print(f"❌ TruffleHog Error: {e}")
        return standard_result("trufflehog", [])