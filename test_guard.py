from core.execution_router import ExecutionRouter

router = ExecutionRouter(mode="paper")

# allowed
print(router.place_order("RELIANCE", "BUY", 5))

# blocked (too large)
print(router.place_order("RELIANCE", "BUY", 500))
