from cart import Product, ShoppingCart
import pytest

@pytest.fixture
def full_cart() -> ShoppingCart:
    example_cart = ShoppingCart()
    
    product_1 = Product("Notebook", 3000)
    product_2 = Product("Teclado", 500)
    
    example_cart.add_products(product_1)
    example_cart.add_products(product_2)
    return example_cart


def test_calculate_total_without_discount(full_cart):
    total_cart = full_cart.calculate_total()
    assert total_cart == 3500


@pytest.mark.parametrize("discount_amount, expected_value", [(10, 3150), (20, 2800)])
def test_calculate_total_with_discount(full_cart, discount_amount, expected_value):
    total_cart = full_cart.calculate_total(discount_amount)
    assert total_cart == expected_value
