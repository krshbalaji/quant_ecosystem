# core/control_api.py

from core.system_registry import registry
from core.meta_intelligence import meta_intelligence
from core.rd_engine import RDEngine
from core.mode_controller import mode_controller

rd_engine = RDEngine()

def get_status():
    return {
        "mode": registry.mode,
        "autonomous": registry.autonomous,
        "risk_enabled": registry.risk_enabled,
        "capital": registry.capital_allocation
    }

def get_regime():
    return registry.last_regime

def set_mode(mode):
    mode_controller.set_mode(mode)
    registry.mode = mode
    return f"Mode switched to {mode}"

from core.system_registry import registry

def evolve_strategy():
    result = rd_engine.evolve()

    # If evolve returns a filename, capture it
    if result:
        registry.active_strategies.append(result)

    return result


def toggle_autonomous(state: bool):
    registry.autonomous = state
    return f"Autonomous mode {'ENABLED' if state else 'DISABLED'}"

def set_capital(percent: int):
    registry.capital_allocation = percent
    return f"Capital allocation set to {percent}%"

def toggle_risk(state: bool):
    registry.risk_enabled = state
    return f"Risk firewall {'ENABLED' if state else 'DISABLED'}"
