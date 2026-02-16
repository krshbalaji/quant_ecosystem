from core.capital_allocator import CapitalAllocator

allocator = CapitalAllocator(capital=100000, risk_per_trade=0.01)

qty = allocator.calculate_qty(
    entry_price=108,
    stop_price=104
)

print("Calculated Qty:", qty)
