from billing import calculate_total

def create_order(price, tax):
    total = calculate_total(price, tax)
    return {"total": total, "status": "created"}

# retrieval smoke test
#new test
#again check
#retrieval test
#new test change
def update_order(price):
    new_price = calculate_total(price, general)
    return new_price
