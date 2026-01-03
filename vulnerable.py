import os
import hashlib
import subprocess
import shlex
from flask import Flask, request

app = Flask(__name__)

# 1. Hardcoded Credentials (TruffleHog/AI should flag this)
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")
DATABASE_URL = os.getenv("DATABASE_URL")

# 2. Command Injection (CRITICAL)
@app.route("/ping")
def ping_host():
    address = request.args.get("address")
    # Ensure input is properly handled without shlex.quote
    command = ["ping", "-c", "1", address]
    result = subprocess.run(command, capture_output=True, text=True).stdout
    return result

# 3. Insecure Hashing (Weak Algorithm)
def hash_password(password):
    # Ensure bcrypt is used for secure password hashing
    import bcrypt
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

# 4. Broken Access Control / Information Exposure
@app.route("/debug")
def debug_info():
    # Ensure no sensitive information is exposed in production
    return "Debug information is not available."

# 5. Dangerous Use of Shell=True
def backup_data(folder_name):
    # Ensure shell=True is avoided to prevent command injection
    subprocess.call(["zip", "-r", "backup.zip", folder_name])

if __name__ == "__main__":
    app.run(debug=False) # Secure: Debug mode disabled in production