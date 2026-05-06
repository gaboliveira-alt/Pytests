
class Product:
    def __init__(self, name: str, price: int) -> None:
        self.name: str = name
        self.price: int = price

class ShoppingCart:
    def __init__(self) -> None:
        self.products: list[Product] = []

    def add_products(self, product: Product) -> None:
        self.products.append(product)

    def calculate_total(self, percentage_discount: int=0) -> float:
        total = sum(product.price for product in self.products)
        
        discount_amount = total * (percentage_discount / 100)
        return total - discount_amount
