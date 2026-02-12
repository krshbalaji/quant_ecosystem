import pandas as pd


class HistoricalBacktester:

    def run(self, strategy, df):

        pnl = 0
        wins = 0
        losses = 0
        equity_curve = []

        for i in range(50, len(df)):

            sub = df.iloc[:i]
            signal, level = strategy.signal(sub)

            if not signal:
                equity_curve.append(pnl)
                continue

            entry = sub.close.iloc[-1]
            sl = level
            target = entry + 2*(entry-sl) if signal=="BUY" else entry - 2*(sl-entry)

            next_close = df.close.iloc[i]

            if signal == "BUY":
                trade_pnl = next_close - entry
            else:
                trade_pnl = entry - next_close

            pnl += trade_pnl

            if trade_pnl > 0:
                wins += 1
            else:
                losses += 1

            equity_curve.append(pnl)

        total = wins + losses
        winrate = (wins/total*100) if total else 0

        return {
            "pnl": round(pnl,2),
            "winrate": round(winrate,2),
            "trades": total,
            "equity_curve": equity_curve
        }
