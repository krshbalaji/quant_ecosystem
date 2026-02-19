from core.system_registry import registry

def generate_advice():
    advice = []

    if registry.mode == "LIVE" and not registry.risk_enabled:
        advice.append("⚠ LIVE mode without risk control.")

    if registry.capital_allocation == 100 and registry.mode == "LIVE":
        advice.append("⚠ Full capital allocation in LIVE mode.")

    if len(list_active()) > 3:
        advice.append("⚠ Too many active strategies.")

    if not advice:
        advice.append("✅ System configuration stable.")

    return advice
