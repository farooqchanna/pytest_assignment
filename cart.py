class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, name, price, qty=1):
        if price < 0 or qty < 1:
            raise ValueError("Invalid price or quantity")
        self.items[name] = (price, qty)

    def total(self):
        return sum(p * q for p, q in self.items.values())

    def count(self):
        return sum(q for _, q in self.items.values())