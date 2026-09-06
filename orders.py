from billing import calculate_total

def create_order(price, tax):
    return calculate_total(price, tax)
