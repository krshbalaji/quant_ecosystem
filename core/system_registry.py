# core/system_registry.py

class SystemRegistry:
    def __init__(self):
        self.mode = "PAPER"
        self.autonomous = False
        self.risk_enabled = True
        self.active_strategies = []
        self.frozen_strategies = []
        self.last_regime = None
        self.capital_allocation = 100
        self.dashboard_message_id = None
        self.dashboard_chat_id = None
        
registry = SystemRegistry()
