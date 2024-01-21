def add_two(a=0,b=0):
    """

    :param a: integer of a
    :param b:  integer of b
    :return: adding a and b
    """
    return a+b
print(help(add_two()))
result = add_two()
print(result) #0
result = add_two(5,9)
print(result)#14
