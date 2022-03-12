
# noinspection PyUnusedLocal
# skus = unicode string

class Product:
    def __init__(self, name: str, price: int, multi: list = [], BxGx: list = [], group: list = []):
        self.name = name
        self.price = price
        self.multi = multi
        self.BxGx = BxGx
        self.group = group

    def __repr__(self):
        return f'{self.name}'


class Item:
    def __init__(self, item: str, quantity: int):
        self.item = products[item]
        self.quantity = quantity

    def __repr__(self):
        return f'{self.quantity}{self.item}'

    def multi_pricing(self) -> int:
        price = []
        count = self.quantity
        offers = self.item.multi

        for offer in sorted(offers, reverse=True):
            # sorted to make sure we apply the highest offer to the basket first.
            multiples = count // offer[0]
            if multiples >= 1:
                price.append(multiples * offer[1])
                count -= multiples * offer[0]

        price.append(count * self.item.price)

        return sum(price)

    def buy_x_get_x(self, basket: list):
        if self.item.BxGx:
            for offer in self.item.BxGx:
                offer = list(offer)
                qualifying_num = int(offer[0])
                priced_item = offer[1]
                free_item_num = int(offer[2])
                free_item = products[offer[3]]

                for target in basket:
                    if target.item.name == free_item.name and target.quantity > 0:
                        if target.item.name == self.item.name:
                            qualifying_num += free_item_num

                        if self.quantity >= qualifying_num:
                            factor = self.quantity // qualifying_num
                            target.quantity -= factor
                            if target.quantity < 0:
                                target.quantity = 0

    def group_discount(self, groups: list):
        if self.item.group:
            for i in range(self.quantity):
                groups.append(self.item)
            self.quantity = 0

    def pricing(self) -> int:
        price = 0
        if self.item.multi:
            price += self.multi_pricing()
        else:
            price += self.item.price * self.quantity

        return price


products = {
    'A': Product('A', 50, multi=[(5, 200), (3, 130)]),
    'B': Product('B', 30, multi=[(2, 45)]),
    'C': Product('C', 20),
    'D': Product('D', 15),
    'E': Product('E', 40, BxGx=['2E1B']),
    'F': Product('F', 10, BxGx=['2F1F']),
    'G': Product('G', 20),
    'H': Product('H', 10, multi=[(5, 45), (10, 80)]),
    'I': Product('I', 35),
    'J': Product('J', 60),
    'K': Product('K', 70, multi=[(2, 120)]),
    'L': Product('L', 90),
    'M': Product('M', 15),
    'N': Product('N', 40, BxGx=['3N1M']),
    'O': Product('O', 10),
    'P': Product('P', 50, multi=[(5, 200)]),
    'Q': Product('Q', 30, multi=[(3, 80)]),
    'R': Product('R', 50, BxGx=['3R1Q']),
    'S': Product('S', 20, group=[(3, 45)]),
    'T': Product('T', 20, group=[(3, 45)]),
    'U': Product('U', 40, BxGx=['3U1U']),
    'V': Product('V', 50, multi=[(2, 90), (3, 130)]),
    'W': Product('W', 20),
    'X': Product('X', 17, group=[(3, 45)]),
    'Y': Product('Y', 20, group=[(3, 45)]),
    'Z': Product('Z', 21, group=[(3, 45)])
}


def checkout(skus: str) -> int:
    """Supermarket checkout function. it accepts a string of products as input and returns the total amount taking into
        account discounted items"""
    if not isinstance(skus, str):
        raise "Items should be a string"

    for product in skus:
        if product not in products:
            return -1

    basket = [Item(i, skus.count(i)) for i in products]

    for item in basket:
        item.buy_x_get_x(basket)

    groups = []
    single_group = []
    group_pricing = 0

    for item in basket:
        item.group_discount(groups)

    groups = sorted(groups, key=lambda x: x.price, reverse=True)
    groups = [i.name for i in groups]

    while groups:
        for i in groups:
            if len(single_group) < products[i].group[0][0]:
                single_group.append(i)
                groups.remove(i)

            if len(single_group) == 3:
                group_pricing += products[i].group[0][1]
                single_group = []

    for i in single_group:
        group_pricing += products[i].price

    prices = [i.pricing() for i in basket]
    total = sum(prices) + group_pricing

    return total

#
# total = checkout('ZSTZ')
#
# print(total)

