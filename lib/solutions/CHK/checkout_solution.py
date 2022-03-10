
# noinspection PyUnusedLocal
# skus = unicode string
"""
In order to complete the round you need to implement the following method:
     checkout(String) -> Integer

Where:
 - param[0] = a String containing the SKUs of all the products in the basket
 - @return = an Integer representing the total checkout value of the items
"""

available_products = ['A', 'B', 'C', 'D']

prices = {'A': 50,
          'B': 30,
          'C': 20,
          'D': 15}


special_offers = {
    'A': (3, 130),
    'B': (2, 45),
}


def checkout(skus: str) -> int:
    """Supermarket checkout function. it accepts a string of products as input and returns the total amount taking into
    account discounted items"""
    if not isinstance(skus, str):
        raise ("Items should be a string")
    for product in skus:
        if product not in available_products:
            return -1

    items = {product: skus.count(product) for product in skus}

    pricing = [items[product] * prices[product] for product in items if product not in special_offers]

    for product, value in special_offers.items():
        price = 0

        if items[product] // value[0] >= 1:
            price += (items[product] // value[0]) * value[1]

        price += (items[product] % value[0]) * prices[product]
        pricing.append(price)

    return sum(pricing)

