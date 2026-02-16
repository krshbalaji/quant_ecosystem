from core.paper_engine import PaperTradingEngine
from brain.decision_engine import DecisionEngine

engine = PaperTradingEngine()
brain = DecisionEngine()

for i in range(5):

    decision = brain.generate_decision()

    order = engine.execute_decision(decision)

    print("Decision:", decision)
    print("Order:", order)
    print("Positions:", engine.get_positions())
    print("------")
