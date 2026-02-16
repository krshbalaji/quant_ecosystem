class BaseMode:
    def __init__(self, engine):
        self.engine = engine

    def run(self):
        raise NotImplementedError
