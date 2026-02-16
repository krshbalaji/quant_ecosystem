"""
Execution Router
Routes orders to correct broker securely
Supports:
- Paper Broker
- FYERS Broker
- Future brokers
"""

from engine.paper_broker import PaperBroker
from engine.fyers_broker import FyersBroker
from core.guard_layer import GuardLayer

class ExecutionRouter:

    def __init__(self, mode="paper"):
        self.mode = mode.lower()
        self.guard = GuardLayer()

        if self.mode == "paper":
            self.broker = PaperBroker()
            print("ExecutionRouter → PAPER broker active")

        elif self.mode == "live":
            self.broker = FyersBroker()
            print("ExecutionRouter → FYERS broker active")

        else:
            raise ValueError(f"Unknown mode: {mode}")


    def place_order(self, symbol, side, qty):

        current_position = self.broker.get_positions().get(symbol, {}).get("qty", 0)

        approved, reason = self.guard.approve_order(
            symbol=symbol,
            side=side,
            qty = int(base_qty * decision["position_multiplier"]),
            current_position=current_position
        )

        if not approved:

            print("GUARD BLOCKED:", reason)

            return {
                "status": "BLOCKED",
                "reason": reason
            }

        order = self.broker.place_order(
            symbol=symbol,
            side=side,
            qty = int(base_qty * decision["position_multiplier"])

        )

        return order



    def get_positions(self):

        return self.broker.get_positions()


    def get_balance(self):

        return self.broker.get_balance()

    from core.performance_tracker import PerformanceTracker

    tracker = PerformanceTracker()

    tracker.record_trade(strategy_name, pnl)
