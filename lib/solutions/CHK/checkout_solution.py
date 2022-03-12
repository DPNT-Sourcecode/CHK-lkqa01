
# noinspection PyUnusedLocal
# skus = unicode string


class Product:
    def __init__(self, name: str, price: int, multi: list = [], BxGx: list = []):
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

    def buy_x_get_x(self, basket: list) -> int:
        price = 0
        offers = self.item.BxGx

        for offer in offers:
            offer = list(offer)
            qualifying_num = int(offer[0])
            priced_item = offer[1]
            free_item_num = int(offer[2])
            free_item = products[offer[3]]

            if priced_item == offer[3]:
                qualifying_num += free_item_num

            target = [x for x in basket if x.item.name == free_item.name and x.quantity > 0]

            if target:
                free_item = target[0]

                if self.quantity >= qualifying_num and free_item.quantity > 0 and priced_item == free_item.item.name:

                    if self.quantity == qualifying_num:
                        factor = 1
                        price = factor * free_item.item.price
                    else:
                        factor = (self.quantity // qualifying_num)
                        price = factor * free_item.item.price

                elif self.quantity >= qualifying_num and free_item.quantity > 0:
                    items_to_remove = self.quantity // qualifying_num

                    if free_item.item.multi:
                        for offer in free_item.item.multi:
                            items_on_offer = items_to_remove // offer[0]
                            items_full_price = items_to_remove % offer[0]

                            price += items_on_offer * offer[1]
                            price += items_full_price * free_item.item.price

                            if items_full_price:
                                if (free_item.quantity // items_full_price) % offer[0] == 0:
                                    price -= items_full_price * offer[1]
                                    price += items_full_price * free_item.item.price

            return price


    def pricing(self, basket: list) -> int:
        price = 0
        if self.item.multi:
            price += self.multi_pricing()
        else:
            price += self.item.price * self.quantity

        if self.item.BxGx:
            price -= self.buy_x_get_x(basket)

        return price


products = {
    'A': Product('A', 50, multi=[(5, 200), (3, 130)]),
    'B': Product('B', 30, multi=[(2, 45)]),
    'C': Product('C', 20),
    'D': Product('D', 15),
    'E': Product('E', 40, BxGx=['2E1B']),
    'F': Product('F', 10, BxGx=['2F1F']),
    'H': Product('H', 10, multi=[(5, 45), (10, 80)]),
    'I': Product('I', 35),
    'J': Product('J', 60),
    'K': Product('K', 80, multi=[(2, 150)]),
    'L': Product('L', 90),
    'M': Product('M', 15),
    'N': Product('N', 40, BxGx=['3N1M']),
    'O': Product('O', 10),
    'P': Product('P', 50, multi=[(5, 200)]),
    'Q': Product('Q', 30, multi=[(3, 80)]),
    'R': Product('R', 50, BxGx=['3R1Q']),
    'S': Product('S', 30),
    'T': Product('T', 20),
    'U': Product('U', 40, BxGx=['3U1U']),
    'V': Product('V', 50, multi=[(2, 90), (3, 130)]),
    'W': Product('W', 20),
    'X': Product('X', 90),
    'Y': Product('Y', 10),
    'Z': Product('Z', 50)
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

    prices = sum([i.pricing(basket) for i in basket])

    return prices

#
# total = checkout('FFF')
#
# print(total)