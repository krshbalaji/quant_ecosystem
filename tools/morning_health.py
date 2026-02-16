import os
import subprocess
from datetime import datetime
from engine.token_manager import TokenManager

def run_health_check():
    print("🩺 Running Morning Health Audit:", datetime.now())

    # 1. Pull latest code
    try:
        subprocess.run(["git", "pull"], check=True)
        print("✅ Git updated")
    except:
        print("⚠ Git pull failed")

    # 2. Install missing packages
    os.system("pip install -r requirements.txt")

    # 3. Refresh Fyers Token
    tm = TokenManager()
    tm.refresh_access_token()

    print("✅ Morning system ready")
