from core.autonomous_selector import AutonomousSelector

selector = AutonomousSelector()

mode = selector.select_mode(
    volatility=0.2,
    heat=30,
    capital_utilization=0.4,
    confidence=0.85
)

print("Selected Mode:", mode)
print("Risk Multiplier:", selector.get_risk_multiplier())
