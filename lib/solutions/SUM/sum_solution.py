# noinspection PyShadowingBuiltins,PyUnusedLocal
# sum(Integer, Integer) -> Integer
"""
Where:
 - param[0] = a positive integer between 0-100
 - param[1] = a positive integer between 0-100
 - @return = an Integer representing the sum of the two numbers
"""


class NumberOutofRange(Exception):
    """Raised when input exceeds the accepted range"""


def compute(x: int, y:int)-> int:
    """Function to compute sum of two integers than are between 0 and 100"""
    if not isinstance(x, int) or not isinstance(y, int):
        raise TypeError('The input should be an integer')

    if not 0 <= x <= 100 or not 0 <= y <= 100:
        raise NumberOutofRange('The input should be between 0 & 100')

    return x+y


