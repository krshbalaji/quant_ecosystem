from infra.telegram_service import send_message, send_menu
from core.mode_controller import set_mode, get_mode

# Optional performance imports
try:
    from core.performance_tracker import (
        get_summary,
        get_equity,
        get_pnl,
        get_trade_count,
    )
except:
    def get_summary(): return "Performance unavailable"
    def get_equity(): return 0
    def get_pnl(): return 0
    def get_trade_count(): return 0


# ============================================
# AI Command Center Controller
# ============================================

def execute_command(cmd):

    cmd = cmd.strip().lower()

    print(f"Telegram command received: {cmd}")

    # --------------------------------
    # Core controls
    # --------------------------------

    if cmd == "/start":

        send_message("🏛 Institutional Quant Ecosystem Online")
        send_menu()

    elif cmd == "/status":

        mode = get_mode()
        send_message(f"System active | Mode: {mode}")

    elif cmd == "/dashboard":

        send_message("Dashboard → http://127.0.0.1:5000")

    elif cmd == "/paper":

        set_mode("PAPER")
        send_message("Switched to PAPER mode")

    elif cmd == "/live":

        set_mode("LIVE")
        send_message("Switched to LIVE mode")

    elif cmd == "/stop":

        set_mode("PAPER")
        send_message("System halted (safe mode)")

    # --------------------------------
    # AI Command Center controls
    # --------------------------------

    elif cmd == "/performance":

        send_message(str(get_summary()))

    elif cmd == "/equity":

        send_message(f"Equity: ₹{get_equity()}")

    elif cmd == "/pnl":

        send_message(f"PNL: ₹{get_pnl()}")

    elif cmd == "/trades":

        send_message(f"Trades: {get_trade_count()}")

    elif cmd == "/leaderboard":

        send_message("Leaderboard → http://127.0.0.1:5000/leaderboard")

    elif cmd == "/sparks":

        send_message("Spark Engine → http://127.0.0.1:5000/sparks")

    elif cmd == "/brain":

        send_message("AI Brain Active | Monitoring Markets")

    elif cmd == "/kill":

        send_message("Emergency stop engaged")
        set_mode("PAPER")

    else:

        send_message("Unknown command")
