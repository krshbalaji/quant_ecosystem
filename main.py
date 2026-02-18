# main.py
# Institutional Production Launcher
# Fast, Threaded, Stable
import webbrowser
import threading
import time
import schedule
from datetime import datetime

from core.system_launcher import SystemLauncher
from core.broker_loader import load_broker
from core.mode_controller import enforce_mode
from core.rd_engine import RDEngine
from core.machine_guard import authorize_machine as verify_machine

from dashboard.app import run_dashboard
from core.telegram_listener import listen as telegram_listen

from tools.morning_health import run_health_check
from core.maintenance import run_daily, should_run
from core.meta_intelligence import MetaIntelligence
from engine.portfolio_manager import PortfolioManager
from core.risk_manager import RiskManager
from data.downloader import HistoricalDownloader
from strategies.orb_strategy import ORBStrategy
from dashboard.app import run_dashboard
from core.live_state import update_state

meta_intelligence = MetaIntelligence()

regime = meta_intelligence.predict_regime()

update_state(
    regime=regime,
    mode=enforce_mode()
)

FAST_BOOT = True
if not FAST_BOOT:
    rd.evolve()

# ================================
# THREAD LAUNCHERS
# ================================

def start_dashboard():
    print("🚀 Starting Institutional Dashboard...")
    run_dashboard()

def open_dashboard():
    time.sleep(2)
    webbrowser.open("http://127.0.0.1:5000/dashboard")

threading.Thread(target=open_dashboard, daemon=True).start()

def start_telegram():
    print("📡 Starting Telegram Control Interface...")
    telegram_listen()


def start_ecosystem():
    print("⚙️ Starting Autonomous Trading Ecosystem...")

    broker = load_broker()

    launcher = SystemLauncher(broker)

    launcher.start()


# ================================
# SCHEDULER ENGINE
# ================================

def scheduler_loop():

    print("⏱ Scheduler Engine Active")

    from infra.secrets import FYERS_CLIENT_ID, FYERS_TOKEN

    downloader = HistoricalDownloader(
    client_id=FYERS_CLIENT_ID,
    token=FYERS_TOKEN
)

    strategy = ORBStrategy()

    broker = load_broker()
    risk = RiskManager(broker)
    pm = PortfolioManager(broker, risk)

    def trading_cycle():

        symbol = "NSE:NIFTYBANK-INDEX"

        try:
            df = downloader.fetch(symbol, timeframe="5")

            signal, sl = strategy.signal(df)

            if signal:
                pm.execute(symbol, signal, df.close.iloc[-1], sl)

        except Exception as e:
            print("Trading cycle error:", e)


    schedule.every(5).minutes.do(trading_cycle)
    schedule.every().day.at("07:00").do(run_health_check)

    while True:

        schedule.run_pending()
        time.sleep(1)


# ================================
# MAIN
# ================================

def main():

    print("="*50)
    print("🏛 Institutional Quant Ecosystem Booting...")
    print("="*50)

    verify_machine()

    mode = enforce_mode()

    print("Mode:", mode)

    if should_run():
        run_daily()

    rd = RDEngine()

    import threading

    def background_ai():
        rd.evolve()
        start_autonomous_engine()

    threading.Thread(target=background_ai, daemon=True).start()


    # THREADS

    threading.Thread(
        target=start_dashboard,
        daemon=True
    ).start()

    threading.Thread(
        target=start_telegram,
        daemon=True
    ).start()

    threading.Thread(
        target=start_ecosystem,
        daemon=True
    ).start()

    threading.Thread(
        target=scheduler_loop,
        daemon=True
    ).start()

    threading.Thread(target=run_dashboard, daemon=True).start()
    
    print("✅ Institutional Ecosystem ACTIVE")

    while True:
        time.sleep(60)


# ================================

if __name__ == "__main__":
    main()
