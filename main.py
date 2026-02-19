import signal
import sys
import time
import threading
import os
from dotenv import load_dotenv

from core.rd_engine import RDEngine
from core.meta_intelligence import meta_intelligence
from core.telegram_listener import listen
from core.autosync import AutoSync
from dashboard.app import app
from core.system_registry import registry

load_dotenv()

shutdown_flag = False


def handle_shutdown(sig, frame):
    global shutdown_flag
    print("\n🛑 Graceful shutdown initiated...")
    shutdown_flag = True
    sys.exit(0)


signal.signal(signal.SIGINT, handle_shutdown)
signal.signal(signal.SIGTERM, handle_shutdown)


def scheduler_loop():
    strategy_folder = "strategies/frozen"

    while True:
        try:
            regime = meta_intelligence.predict_regime()
            registry.last_regime = regime

            print(f"Scheduler Check → Regime: {regime}")

            time.sleep(10)

        except Exception as e:
            print("Scheduler error:", e)
            time.sleep(5)


def main():
    print("🚀 Booting Institutional Ecosystem...")

    rd = RDEngine()
    rd.evolve()

    threading.Thread(target=listen, daemon=True).start()
    threading.Thread(target=scheduler_loop, daemon=True).start()

    autosync = AutoSync(interval=600, auto_start=True)
    autosync.start()

    print("✅ Institutional Ecosystem ACTIVE")
    print("🌐 Dashboard running at http://127.0.0.1:5000")

    app.run(host="0.0.0.0", port=5000, debug=False)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Graceful shutdown complete.")
        sys.exit(0)
