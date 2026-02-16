class IntelligenceEngine:

    def __init__(
        self,
        broker,
        portfolio,
        heat_engine,
        capital_allocator,
        max_heat=60,
        risk_tolerance=0.02
    ):

        self.broker = broker
        self.portfolio = portfolio
        self.heat_engine = heat_engine
        self.capital_allocator = capital_allocator

        from core.strategy_brain import StrategyBrain
        from core.self_learning_engine import SelfLearningEngine
        from core.learning_engine import LearningEngine
        from core.aggression_engine import AggressionEngine
        from core.autonomous_selector import AutonomousSelector

        self.selector = AutonomousSelector()
        self.aggression_engine = AggressionEngine()
        self.strategy_brain = StrategyBrain()
        self.learning_engine = SelfLearningEngine(self.strategy_brain)
        self.learning_engine = LearningEngine()

        # Adaptive parameters
        self.max_heat = max_heat
        self.risk_tolerance = risk_tolerance

        # Learning memory
        self.trade_history = []

        print("Adaptive Intelligence Engine Activated")

    # -------------------------------
    # Portfolio heat check
    # -------------------------------
    def check_portfolio_heat(self):

        heat = self.heat_engine.calculate_heat()

        if heat >= self.max_heat:
            return False, heat

        return True, heat

        mode = self.selector.select_mode(
            volatility=volatility,
            heat=heat,
            capital_utilization=capital/self.capital_allocator.total_capital,
            confidence=score
        )

        risk_multiplier = self.selector.get_risk_multiplier()

        capital *= risk_multiplier


    # -------------------------------
    # Capital allocation check
    # -------------------------------
    def check_capital(self, symbol):

        price = self.broker.get_quote(symbol)

        capital = self.capital_allocator.allocate(price)

        if capital <= 0:
            return False, capital

        return True, capital


    # -------------------------------
    # Decision scoring logic
    # -------------------------------
    def compute_score(self, signal_strength, volatility, heat):

        score = (
            signal_strength * 0.5
            + (1 - volatility) * 0.3
            + (1 - heat / 100) * 0.2
        )

        return score


    # -------------------------------
    # Learning engine
    # -------------------------------
    def learn(self, decision):

        self.trade_history.append(decision)

        if len(self.trade_history) > 100:
            self.trade_history.pop(0)


    # -------------------------------
    # Main approval engine
    # -------------------------------
    def approve_trade(self, symbol, strategy, signal_strength, volatility):

        weight = self.strategy_brain.get_weight(strategy)

        adjusted_signal = signal_strength * weight

        score = adjusted_signal * (1 - volatility)

        capital = self.capital_allocator.allocate(symbol)
        
        score = float(round(score, 2))
        capital = float(round(capital, 2))
        strategy_weight = float(round(weight, 2))
        
        decision = {
            "approved": True,
            "score": round(score, 2),
            "capital": round(capital, 2),
            "mode": mode,
            "strategy_weight": strategy_weight
        }


        aggression = self.aggression_engine.calculate_aggression(
            strategy_confidence=strategy_weight,
            learning_confidence=learning_confidence,
            capital_strength=min(capital / self.capital_allocator.total_capital, 1),
            heat=heat,
            volatility=volatility
        )
       
        decision["aggression_mode"] = aggression["mode"]
        decision["aggression_score"] = aggression["score"]
        decision["position_multiplier"] = aggression["position_multiplier"]

        return decision

        if decision["approved"]:
            self.learning_engine.record_trade(
                symbol,
                decision["score"],
                0   # outcome unknown initially
        )

        # learning layer
        self.learn(decision)

        return decision

        core.learning_engine.learn_from_trade(
            strategy="ema_ribbon",
            entry_price=100,
            exit_price=105,
            qty=10
        )
