# core/mobile_command.py

from core.mode_controller import mode_controller
from infra.telegram_service import send_message


def execute_command(cmd: str):
    """
    Handles Telegram commands safely.
    """

    try:

        cmd = cmd.strip().lower()

        # STATUS
        if cmd == "/status":

            mode = mode_controller.get_mode()

            send_message(
                f"System operational\n"
                f"Mode: {mode}\n"
                f"Guardian: Active\n"
                f"Engine: Running"
            )

        # DASHBOARD
        elif cmd == "/dashboard":

            send_message(
                "Dashboard ready:\n"
                "http://127.0.0.1:5000/dashboard"
            )

        # SWITCH TO LIVE
        elif cmd == "/live":

            mode_controller.set_mode("LIVE")

            send_message("Switched to LIVE mode")

        # SWITCH TO PAPER
        elif cmd == "/paper":

            mode_controller.set_mode("PAPER")

            send_message("Switched to PAPER mode")

        # LEADERBOARD
        elif cmd == "/leaderboard":

            send_message(
                "Leaderboard:\n"
                "http://127.0.0.1:5000/leaderboard"
            )

        # SPARK ENGINE
        elif cmd == "/sparks":

            send_message(
                "Spark Engine:\n"
                "http://127.0.0.1:5000/sparks"
            )

        # PERFORMANCE
        elif cmd == "/performance":

            send_message(
                "Performance Dashboard:\n"
                "http://127.0.0.1:5000/performance"
            )

        # STOP
        elif cmd == "/stop":

            send_message("System stop command acknowledged")

        # UNKNOWN
        else:

            send_message("Unknown command")

    except Exception as e:

        send_message(f"Command error: {str(e)}")
