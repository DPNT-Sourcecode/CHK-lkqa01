# noinspection PyShadowingBuiltins,PyUnusedLocal
# sum(Integer, Integer) -> Integer
"""
Where:
 - param[0] = a positive integer between 0-100
 - param[1] = a positive integer between 0-100
 - @return = an Integer representing the sum of the two numbers
"""


def compute(x: int, y:int)-> int:
    if not isinstance(x, int) or not isinstance(y, int):
        raise TypeError('The input should be an integer')

    if not 0 < x < 100
    return x+y



