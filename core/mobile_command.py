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

    elif cmd == "/brain":
        from core.hedge_allocator import HedgeAllocator
        allocator = HedgeAllocator()
        ranking = allocator.rank_strategies()
        return str(ranking[:5])

    elif cmd.startswith("/manual"):
        parts = cmd.split()
        if len(parts) > 1:
            control_state.set_manual(parts[1])
            return f"Manual mode enabled → {parts[1]}"

    elif cmd == "/auto":
        control_state.set_auto()
        return "Returned to FULL AUTONOMOUS mode"


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
