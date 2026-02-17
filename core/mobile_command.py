from core.mode_controller import mode_controller
from infra.telegram_service import send_message


def execute_command(cmd):

    cmd = cmd.lower()

    if cmd == "/start":
        send_message(
            "🏛 Institutional Control Panel Active\n\n"
            "/status\n"
            "/mode\n"
            "/paper\n"
            "/live\n"
            "/performance\n"
            "/strategies\n"
            "/stop"
        )


    elif cmd == "/status":

        mode = mode_controller.get_mode()

        send_message(
            f"System Status:\n"
            f"Mode: {mode}\n"
            f"Engine: ACTIVE"
        )


    elif cmd == "/paper":

        mode_controller.set_mode("PAPER")

        send_message("Switched to PAPER mode")


    elif cmd == "/live":

        mode_controller.set_mode("LIVE")

        send_message("LIVE mode enabled")


    elif cmd == "/performance":

        import json

        try:
            with open("data/performance.json") as f:
                perf = json.load(f)

            send_message(str(perf))

        except:
            send_message("No performance data yet")


    elif cmd == "/strategies":

        import json

        try:
            with open("data/elite.json") as f:
                elite = json.load(f)

            msg = "Top Strategies:\n"

            for s in elite[:5]:
                msg += f"{s.get('name')} score:{s.get('score')}\n"

            send_message(msg)

        except:
            send_message("No strategies yet")


    elif cmd == "/stop":

        mode_controller.set_mode("PAPER")

        send_message("Emergency STOP activated")


    else:

        send_message("Unknown command")

elif cmd == "/performance":
    from core.performance_tracker import get_summary
    send_message(str(get_summary()))

elif cmd == "/equity":
    from core.performance_tracker import get_equity
    send_message(f"Equity: ₹{get_equity()}")

elif cmd == "/pnl":
    from core.performance_tracker import get_pnl
    send_message(f"PNL: ₹{get_pnl()}")

elif cmd == "/trades":
    from core.performance_tracker import get_trade_count
    send_message(f"Trades: {get_trade_count()}")

elif cmd == "/leaderboard":
    send_message("Dashboard → http://127.0.0.1:5000/leaderboard")

elif cmd == "/sparks":
    send_message("Spark Engine → http://127.0.0.1:5000/sparks")
