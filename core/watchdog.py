import time


class Watchdog:

    def __init__(self):

        self.last_heartbeat = time.time()


    def beat(self):

        self.last_heartbeat = time.time()


    def alive(self):

        return time.time() - self.last_heartbeat < 600
