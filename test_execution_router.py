from core.execution_router import ExecutionRouter
from core.capital_allocator import CapitalAllocator


router = ExecutionRouter()

allocator = CapitalAllocator(100000)

symbol = "RELIANCE"

price = router.broker.get_quote(symbol)

qty = allocator.calculate_qty(price)

order = router.place_order(
    symbol=symbol,
    side="BUY",
    qty=qty
)

print(order)
print(router.broker.get_positions())
