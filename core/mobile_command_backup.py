from infra.telegram_service import send_message
from core.mode_controller import mode_controller
import os


def handle_command(command):
    command = command.strip().lower()

    print(f"Received command: {command}")

    if command == "/start":
        send_message("📊 Institutional Control Panel Activated.")

    elif command == "/status":
        send_message("📡 System is ACTIVE.")

    elif command == "/dashboard":
        send_message("🌐 Dashboard: http://127.0.0.1:5000")

    elif command == "/paper":
        mode_controller.set_mode("PAPER")
        send_message("📝 Switched to PAPER mode.")

    elif command == "/live":
        mode_controller.set_mode("LIVE")
        send_message("🚀 Switched to LIVE mode.")

    elif command == "/leaderboard":
        send_message("🏆 Leaderboard feature coming soon.")

    elif command == "/sparks":
        send_message("⚡ Sparks module initializing.")

    elif command == "/stop":
        send_message("🛑 System shutting down.")
        os._exit(0)

    else:
        send_message("Unknown command.")
