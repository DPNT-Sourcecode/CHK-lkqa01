

# noinspection PyUnusedLocal
# friend_name = unicode string

"""
In order to complete the round you need to implement the following method:
     hello(String) -> String

Where:
 - param[0] = a String. Ignore for now.
 - @return = a String containing a message

"""


def hello(friend_name: float = None) -> str:
    """Function to greet the user, takes a string and return Hello, 'string'"""
    if not isinstance(friend_name, str):
        raise TypeError("this function expects a string as input")
    return f'Hello, {friend_name}!'


if __name__ == '__main__':
    print(hello(friend_name))