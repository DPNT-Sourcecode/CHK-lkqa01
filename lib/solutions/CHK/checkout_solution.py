
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



def checkout(skus: str) -> int:
    """Supermarket checkout function. it accepts a string of products as input and returns the total amount taking into
    account discounted items"""
    for product in skus:
        if product not in available_products:
            return -1

    items = {product:skus.count(product) for product in skus}
    print(items)



print(checkout('AAABBCD'))
