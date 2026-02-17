# core/mobile_command.py

from core.mode_controller import set_mode, get_mode


def init():
    print("Mobile command interface initialized")


def execute_command(command: str):

    command = command.lower().strip()

    if command == "/paper":
        set_mode("PAPER")
        return "Switched to PAPER mode"

    elif command == "/live":
        set_mode("LIVE")
        return "Switched to LIVE mode"

    elif command == "/backtest":
        set_mode("BACKTEST")
        return "Switched to BACKTEST mode"

    elif command == "/mode":
        return f"Current mode: {get_mode()}"

    elif command == "/status":
        return "System operational"

    elif command == "/dashboard":
        return "Dashboard: http://127.0.0.1:5000"

    elif command == "/help":
        return (
            "Commands:\n"
            "/paper\n"
            "/live\n"
            "/backtest\n"
            "/mode\n"
            "/status\n"
            "/dashboard"
        )

    return "Unknown command"
