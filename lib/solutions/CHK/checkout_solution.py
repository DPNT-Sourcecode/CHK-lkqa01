
# noinspection PyUnusedLocal
# skus = unicode string


class Product:
    def __init__(self, name: str, price: int, multi: list=[], BxGx: list=[]):
        self.name = name
        self.price = price
        self.multi = multi
        self.BxGx = BxGx

    def __repr__(self):
        return f'{self.name}'


class Item:
    def __init__(self, item: str, quantity: int):
        self.item = products[item]
        self.quantity = quantity

    def __repr__(self):
        return f'{self.quantity}{self.item}'

    def pricing(self):
        pass


products = {
    'A': Product('A', 50, multi=[(5, 200), (2, 120)]),
    'B': Product('B', 30, multi=[(2, 45)]),
    'C': Product('C', 20),
    'D': Product('D', 15),
    'E': Product('E', 40, BxGx=["CODED"]) #Come to this later.
}


def checkout(skus: str) -> int:
    """Supermarket checkout function. it accepts a string of products as input and returns the total amount taking into
    account discounted items"""
    if not isinstance(skus, str):
        raise "Items should be a string"

    for product in skus:
        if product not in product:
            return -1

    basket = [Item(i, skus.count(i)) for i in product]
    print(basket)

    pricing = sum([i.pricing() for i in basket])

    return pricing


# sum2 = checkout('A')
# print(sum)