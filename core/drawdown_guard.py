class DrawdownGuard:

    def __init__(self, max_dd=0.15):
        self.max_dd = max_dd
        self.peak = 0
        self.active = True

    def update(self, equity):

        if equity > self.peak:
            self.peak = equity

        dd = (self.peak - equity) / max(1, self.peak)

        if dd >= self.max_dd:
            self.active = False

        return self.active
