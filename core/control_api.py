# core/control_api.py

from core.system_registry import registry
from core.meta_intelligence import meta_intelligence
from core.rd_engine import RDEngine
from core.mode_controller import mode_controller
from core.state_engine import state_engine
rd_engine = RDEngine()

def get_status():
    return state_engine.state

def get_regime():
    return registry.last_regime

def set_mode(mode):
    state_engine.state["mode"] = mode
    state_engine.save_state()

from core.system_registry import registry

def evolve_strategy():
    result = rd_engine.evolve()

    # If evolve returns a filename, capture it
    if result:
        registry.active_strategies.append(result)

    return result


def toggle_autonomous(value=None):
    if value is None:
        state_engine.state["autonomous"] = not state_engine.state["autonomous"]
    else:
        state_engine.state["autonomous"] = bool(value)

    state_engine.save_state()

def set_capital(percent):
    state_engine.state["capital_allocation"] = percent
    state_engine.state["capital"] = percent
    state_engine.save_state()

def toggle_risk(value=None):
    if value is None:
        state_engine.state["risk_enabled"] = not state_engine.state["risk_enabled"]
    else:
        state_engine.state["risk_enabled"] = bool(value)

    state_engine.save_state()

def soft_stop():
    state_engine.state["autonomous"] = False
    state_engine.save_state()


def hard_stop():
    state_engine.state["autonomous"] = False
    state_engine.state["risk_enabled"] = False
    state_engine.state["capital_allocation"] = 0
    state_engine.save_state()