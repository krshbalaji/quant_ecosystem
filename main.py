# main.py
import signal
import sys
from core.rd_engine import RDEngine
from core.mode_controller import mode_controller
from core.meta_intelligence import meta_intelligence
from dashboard.app import app
import threading
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

import time

def scheduler_loop():
    print("⏱ Scheduler Engine Active")

    while True:
        try:
            from core.meta_intelligence import meta_intelligence

            regime = meta_intelligence.predict_regime()
            print(f"Scheduler Check → Regime: {regime}")

            time.sleep(30)  # check every 30 seconds

        except Exception as e:
            print("Scheduler error:", e)
            time.sleep(30)
      
if __name__ == "__main__":
    main()
