import importlib
import os
import requests
import socket
import yaml

print("\n==============================")
print("   QUANT ECOSYSTEM CHECK")
print("==============================\n")

def check_module(name):
    try:
        importlib.import_module(name)
        print(f"✅ Module OK: {name}")
    except Exception as e:
        print(f"❌ Module FAIL: {name} → {e}")

def check_file(path):
    if os.path.exists(path):
        print(f"✅ File OK: {path}")
    else:
        print(f"❌ Missing File: {path}")

def check_port(port=5000):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex(("127.0.0.1", port))
    if result == 0:
        print(f"⚠ Port {port} already in use")
    else:
        print(f"✅ Port {port} free")
    s.close()
    
def auto_fix():
    print("🔧 Attempting auto repair...")
    os.system("pip install -r requirements.txt")

print("📦 Checking Core Modules")
for mod in [
    "flask", "pandas", "numpy",
    "matplotlib", "schedule",
    "requests", "yaml"
]:
    check_module(mod)

print("\n📁 Checking Required Files")
for f in [
    "main.py",
    "engine/runner.py",
    "engine/fyers_broker.py",
    "engine/risk_manager.py",
    "dashboard/web_dashboard.py",
    "config/settings.yaml"
]:
    check_file(f)

print("\n🔐 Checking Fyers Auth")
try:
    with open("config/secrets.yaml") as f:
        secrets = yaml.safe_load(f)
    token = secrets["fyers"]["access_token"]
    client = secrets["fyers"]["client_id"]

    if token and client:
        print("✅ Fyers credentials present")
    else:
        print("❌ Fyers credentials missing")
except:
    print("❌ Cannot read secrets.yaml")

print("\n📡 Checking Telegram")
try:
    bot = secrets["telegram"]["bot_token"]
    chat = secrets["telegram"]["chat_id"]
    if bot and chat:
        print("✅ Telegram credentials present")
    else:
        print("❌ Telegram credentials missing")
except:
    print("❌ Telegram not configured")

print("\n🌐 Checking Dashboard Port")
check_port(5000)

print("\n📊 Checking Downloader")
try:
    from data.downloader import HistoricalDownloader
    print("✅ Downloader import OK")
except Exception as e:
    print("❌ Downloader FAIL:", e)

print("\n🧠 Checking Optimizer")
try:
    from optimizer.walkforward_optimizer import WalkForwardOptimizer
    print("✅ WalkForward optimizer OK")
except:
    print("⚠ WalkForward optimizer missing")

print("\n🎯 Checking Strategy Loader")
try:
    from optimizer.strategy_loader import load_strategies
    print("✅ Strategy loader OK")
except:
    print("⚠ Strategy loader missing")

print("\n🛡 Checking Risk Manager")
try:
    from engine.risk_manager import RiskManager
    print("✅ Risk Manager OK")
except:
    print("❌ Risk Manager FAIL")

print("\n==============================")
print("   CHECK COMPLETE")
print("==============================\n")
