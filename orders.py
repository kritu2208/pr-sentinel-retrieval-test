from billing import calculate_total

def create_order(price, tax):
    total = calculate_total(price, tax)
    return {"total": total}
