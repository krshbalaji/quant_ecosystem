# main.py
import signal
import sys
import time
import threading
import os
from core.rd_engine import RDEngine
from core.mode_controller import mode_controller
from core.meta_intelligence import meta_intelligence
from dashboard.app import app
from core.telegram_listener import listen as telegram_listener


shutdown_flag = False

def handle_shutdown(sig, frame):
    global shutdown_flag
    print("\n🛑 Graceful shutdown initiated...")
    shutdown_flag = True
    sys.exit(0)

signal.signal(signal.SIGINT, handle_shutdown)
signal.signal(signal.SIGTERM, handle_shutdown)

from core.system_launcher import SystemLauncher
from dashboard.app import run_dashboard


def main():

    # Initialize engines
    rd = RDEngine()
    rd.evolve()

    # Start background systems
    threading.Thread(target=telegram_listener, daemon=True).start()
    threading.Thread(target=scheduler_loop, daemon=True).start()

    print("✅ Institutional Ecosystem ACTIVE")

    # Run Flask in main thread
    app.run(host="0.0.0.0", port=5000, debug=False)

from dashboard.app import app
print("🚀 Institutional Dashboard running at http://127.0.0.1:5000")


def scheduler_loop():
    strategy_folder = "strategies/frozen"

    while True:
        try:
            regime = meta_intelligence.predict_regime()
            print(f"Scheduler Check → Regime: {regime}")

            if not os.path.exists(strategy_folder):
                time.sleep(5)
                continue

            for file in os.listdir(strategy_folder):
                if file.endswith(".py"):
                    print(f"Running: {file}")

            time.sleep(10)

        except Exception as e:
            print("Scheduler error:", e)
            time.sleep(5)

      
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Graceful shutdown initiated")
        sys.exit(0)

