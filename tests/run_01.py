
def fetch_discount_rate() -> float:
    return 0.10

def get_discount(price: float) -> float:
    discount_rate = fetch_discount_rate()
    return price - (price * discount_rate)