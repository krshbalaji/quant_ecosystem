from datetime import datetime


class KillSwitch:

    def __init__(self, daily_loss_limit=0.05):
        self.daily_loss_limit = daily_loss_limit
        self.start_equity = None

    def check(self, current_equity):

        if self.start_equity is None:
            self.start_equity = current_equity

        loss = (self.start_equity - current_equity) / self.start_equity

        if loss >= self.daily_loss_limit:
            return True

        return False
