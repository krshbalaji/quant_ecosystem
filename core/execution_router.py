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
from core.adaptive_allocator import AdaptiveAllocator
from core.portfolio_optimizer import PortfolioOptimizer
from core.rl_allocator import RLAllocator
from core.drl_allocator import DRLAllocator
from core.lstm_predictor import LSTMPredictor
from core.lstm_gpu import LSTMGPU
from core.compounding_engine import CompoundingEngine
from core.drawdown_recovery import DrawdownRecovery


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

        allocator = AdaptiveAllocator(broker)
        allocation = allocator.allocate(strategy_name)

        qty = int(allocation / price)

        optimizer = PortfolioOptimizer(broker)

        allocation_map = optimizer.optimize()

        allocation = allocation_map.get(strategy_name, broker.get_balance() * 0.01)

        qty = int(allocation / price)

        drl = DRLAllocator(broker)

        allocation_map = drl.allocate()

        allocation = allocation_map.get(strategy_name, broker.get_balance() * 0.01)

        predictor = LSTMPredictor()

        prediction = predictor.predict(price_history)

        if prediction == 0:

            print("LSTM: no clear direction → skip trade")

            return

        if prediction == 1 and signal != "BUY":

            print("LSTM blocked SELL")

            return

        if prediction == -1 and signal != "SELL":

            print("LSTM blocked BUY")

            return

        lstm = LSTMGPU()

        prediction = lstm.predict(price_history)

        if prediction != signal_direction:

            print("GPU LSTM blocked weak trade")

            return

        import json

        control = json.load(open("data/system_control.json"))

        if not control["trading_enabled"]:

            print("Trading disabled by mobile command")

            return
        
        rl_allocator = RLAllocator(broker)

        allocation_map = rl_allocator.allocate()

        allocation = allocation_map.get(strategy_name, broker.get_balance() * 0.01)

        qty = recovery.position_size(price)

        compound = CompoundingEngine(broker)
        
        recovery = DrawdownRecovery(broker)


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
    
    rl_allocator.update(strategy_name, pnl)

    drl.update(strategy_name, pnl)

    predictor.train(price_history, pnl)

    lstm.train(price_history)
