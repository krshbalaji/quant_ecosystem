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
