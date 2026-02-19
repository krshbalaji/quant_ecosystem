from infra.telegram_service import edit_message, send_message
from core.control_api import get_status, get_regime, set_mode, toggle_risk, toggle_autonomous, evolve_strategy
from core.system_registry import registry
from core.strategy_manager import list_active, list_frozen, activate_strategy, freeze_strategy


def open_dashboard(chat_id):
    text, keyboard = build_main_dashboard()

    response = send_message(text)

    if response and "result" in response:
        registry.dashboard_message_id = response["result"]["message_id"]
        registry.dashboard_chat_id = chat_id
        edit_message(chat_id, registry.dashboard_message_id, text, keyboard)

# -----------------------
# Dashboard Builder
# -----------------------

def build_main_dashboard():
    status = get_status()
    regime = get_regime()

    text = (
        "📟 INSTITUTIONAL TRADING TERMINAL\n"
        "────────────────────────────\n\n"
        f"Mode: {status['mode']}\n"
        f"Regime: {regime}\n"
        f"Risk: {'ON' if status['risk_enabled'] else 'OFF'}\n"
        f"Autonomous: {'ON' if status['autonomous'] else 'OFF'}\n"
        f"Capital: {status['capital']}%\n"
        f"Active Strategies: {len(registry.active_strategies)}\n\n"
        "────────────────────────────"
    )

    keyboard = {
        "inline_keyboard": [
            [
                {"text": "⚙ Execution", "callback_data": "execution_panel"},
                {"text": "🛡 Risk", "callback_data": "risk_panel"}
            ],
            [
                {"text": "🧠 Strategy", "callback_data": "strategy_panel"},
                {"text": "🚀 Autonomous", "callback_data": "auto_panel"}
            ]
        ]
    }

    return text, keyboard


# -----------------------
# Panel Builders
# -----------------------

def build_execution_panel():
    status = get_status()
    text = (
        "⚙ EXECUTION CONTROL\n"
        "────────────────────────\n\n"
        f"Current Mode: {status['mode']}\n"
    )

    keyboard = {
        "inline_keyboard": [
            [{"text": "Switch to PAPER", "callback_data": "set_paper"}],
            [{"text": "Switch to LIVE", "callback_data": "confirm_live"}],
            [{"text": "🔙 Back", "callback_data": "main"}]
        ]
    }

    return text, keyboard


def build_risk_panel():
    status = get_status()
    text = (
        "🛡 RISK CONTROL\n"
        "────────────────────────\n\n"
        f"Risk: {'ON' if status['risk_enabled'] else 'OFF'}\n"
        f"Capital: {status['capital']}%\n"
    )

    keyboard = {
        "inline_keyboard": [
            [{"text": "Toggle Risk", "callback_data": "toggle_risk"}],
            [
                {"text": "25%", "callback_data": "capital_25"},
                {"text": "50%", "callback_data": "capital_50"},
                {"text": "100%", "callback_data": "capital_100"}
            ],
            [{"text": "🔙 Back", "callback_data": "main"}]
        ]
    }

    return text, keyboard


def build_strategy_panel():
    active = list_active()
    frozen = list_frozen()

    text = "🧠 STRATEGY CONTROL\n"
    text += "────────────────────────\n\n"

    text += "Active:\n"
    for s in active:
        text += f"• {s}\n"

    text += "\nFrozen:\n"
    for s in frozen:
        text += f"• {s}\n"

    keyboard = {
        "inline_keyboard": []
    }

    for s in frozen[:5]:  # limit to avoid Telegram overflow
        keyboard["inline_keyboard"].append(
            [{"text": f"Activate {s}", "callback_data": f"activate_{s}"}]
        )

    for s in active[:5]:
        keyboard["inline_keyboard"].append(
            [{"text": f"Freeze {s}", "callback_data": f"freeze_{s}"}]
        )

    keyboard["inline_keyboard"].append(
        [{"text": "🔙 Back", "callback_data": "main"}]
    )

    return text, keyboard


def build_auto_panel():
    status = get_status()

    text = (
        "🚀 AUTONOMOUS CONTROL\n"
        "────────────────────────\n\n"
        f"Autonomous: {'ON' if status['autonomous'] else 'OFF'}\n"
    )

    keyboard = {
        "inline_keyboard": [
            [{"text": "Toggle Autonomous", "callback_data": "toggle_auto"}],
            [{"text": "🔙 Back", "callback_data": "main"}]
        ]
    }

    return text, keyboard


# -----------------------
# Callback Router
# -----------------------

def handle_callback(data, chat_id):

    msg_id = registry.dashboard_message_id

    if data == "main":
        text, keyboard = build_main_dashboard()

    elif data == "execution_panel":
        text, keyboard = build_execution_panel()

    elif data == "risk_panel":
        text, keyboard = build_risk_panel()

    elif data == "strategy_panel":
        text, keyboard = build_strategy_panel()

    elif data == "auto_panel":
        text, keyboard = build_auto_panel()

    elif data == "set_paper":
        set_mode("PAPER")
        text, keyboard = build_execution_panel()

    elif data == "confirm_live":
        text = "⚠ Confirm LIVE mode?"
        keyboard = {
            "inline_keyboard": [
                [{"text": "✅ Confirm LIVE", "callback_data": "set_live"}],
                [{"text": "❌ Cancel", "callback_data": "execution_panel"}]
            ]
        }

    elif data == "set_live":
        set_mode("LIVE")
        text, keyboard = build_execution_panel()

    elif data == "toggle_risk":
        toggle_risk(not get_status()['risk_enabled'])
        text, keyboard = build_risk_panel()

    elif data == "toggle_auto":
        toggle_autonomous(not get_status()['autonomous'])
        text, keyboard = build_auto_panel()

    elif data.startswith("capital_"):
        percent = int(data.split("_")[1])
        registry.capital_allocation = percent
        text, keyboard = build_risk_panel()

    elif data == "evolve":
        new_strategy = evolve_strategy()
        text = f"🧠 New Strategy Evolved:\n\n{new_strategy}"
        keyboard = {
            "inline_keyboard": [
                [{"text": "🔙 Back", "callback_data": "strategy_panel"}]
            ]
        }

    elif data.startswith("activate_"):
        name = data.replace("activate_", "")
        activate_strategy(name)
        text, keyboard = build_strategy_panel()

    elif data.startswith("freeze_"):
        name = data.replace("freeze_", "")
        freeze_strategy(name)
        text, keyboard = build_strategy_panel()

    else:
        text, keyboard = build_main_dashboard()

    edit_message(chat_id, msg_id, text, keyboard)
