Confidence Score =
    (Rolling Sharpe * 0.3)
  + (Regime Coverage Score * 0.2)
  + (Low Drawdown Stability * 0.2)
  + (Paper vs Real Similarity * 0.2)
  + (Live Consistency * 0.1)

if confidence > 0.75:
    recommendation = "Switch to FULL REAL"
elif confidence > 0.60:
    recommendation = "Hybrid Mode"
else:
    recommendation = "Paper Continue"

🧠 SYSTEM CONFIDENCE HIGH

Score: 0.81
Sharpe: 1.42
Drawdown: 2.1%
Regime Stability: Strong

Recommendation:
Switch to FULL REAL mode?

Reply:
YES_REAL
or
CONTINUE_PAPER
