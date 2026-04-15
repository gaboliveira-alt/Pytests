
def fetch_discount_rate(initial_value: float) -> float:
    return 0.10 * initial_value

def get_discount(price: float) -> float:
    discount_rate = fetch_discount_rate(0.9)
    return price - (price * discount_rate)