def fact(number: int, a: int) -> int:
    """
    Function for factorial calculation.

    :param number: the number whose factorial we want to calculate
    :param a: help number to calculate

    :raises ValueError: if number < 0

    :return: factorial
    """
    a = a * number
    if number > 1:
        return fact(number - 1, a)
    elif number == 1 or number == 0:
        return a
    else:
        raise ValueError(f"You cannot take a factorial from the number {number}")


n = int(input('Enter a number: '))

print(f'Result: {fact(n, 1)}')
