import pytest
from cart import ShoppingCart


@pytest.fixture
def cart():
    cart = ShoppingCart()
    cart.add_item("pen", 50, qty=2)
    cart.add_item("notebook", 200)
    return cart


def test_total(cart):
    assert cart.total() == 300


def test_count(cart):
    assert cart.count() == 3


def test_new_cart_total():
    new_cart = ShoppingCart()
    assert new_cart.total() == 0


def test_negative_price_raises():
    cart = ShoppingCart()

    with pytest.raises(ValueError):
        cart.add_item("pen", -50)