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

def execute_command(cmd, chat_id):
    cmd = cmd.strip().lower()

    if cmd == "/start":
        return "🏛 Institutional Hedge Fund Terminal Ready"

    elif cmd == "/mode":
        from core.mode_controller import mode_controller
        return f"Current Mode: {mode_controller.get_mode()}"

    elif cmd == "/equity":
        try:
            from core.performance_tracker import performance_tracker
            return f"Equity: ₹{performance_tracker.current_equity}"
        except:
            return "Equity data unavailable"

    elif cmd == "/performance":
        try:
            from core.performance_tracker import performance_tracker
            return performance_tracker.summary()
        except:
            return "Performance data unavailable"

    elif cmd == "/regime":
        from core.meta_intelligence import meta_intelligence
        return f"Market Regime: {meta_intelligence.current_regime}"

    elif cmd == "/evolve":
        from core.rd_engine import RDEngine
        rd = RDEngine()
        rd.evolve()
        return "New strategy evolved."

    elif cmd == "/status":
        return "System ACTIVE"

    else:
        return "Unknown command"


    MENU = [
    ["/status", "/dashboard"],
    ["/paper", "/live"],
    ["/performance", "/regime"],
    ["/leaderboard", "/telemetry"],
    ["/stop"]
]
