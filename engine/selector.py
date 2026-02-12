class Selector:

    def choose(self, results):
        results.sort(key=lambda x: x["sharpe"], reverse=True)
        return results[:5]
