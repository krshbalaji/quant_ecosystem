import numpy as np

class HealthEngine:

    def __init__(self, portfolio):
        self.portfolio = portfolio
        pass

    def compute_health_score(self):
        sharpe = self.portfolio.sharpe()
        dd = self.portfolio.max_drawdown()

        score = (sharpe * 0.6) + ((1 + dd) * 0.4)
        return round(score, 1)
        
    def calculate(self, metrics):
        """
        metrics dict requires:
        {
            "rolling_sharpe": float,
            "drawdown": float,
            "ml_confidence": float,  # 0 to 1
            "win_rate": float,       # 0 to 1
            "volatility": float      # normalized 0 to 1
        }
        """

        sharpe_score = np.clip((metrics["rolling_sharpe"] + 1) / 2, 0, 1)
        drawdown_score = np.clip(1 - abs(metrics["drawdown"]), 0, 1)
        ml_score = np.clip(metrics["ml_confidence"], 0, 1)
        win_score = np.clip(metrics["win_rate"], 0, 1)
        vol_score = np.clip(1 - metrics["volatility"], 0, 1)

        total = (
            sharpe_score * 0.30 +
            drawdown_score * 0.25 +
            ml_score * 0.20 +
            win_score * 0.15 +
            vol_score * 0.10
        )

        return round(total * 100, 2)
