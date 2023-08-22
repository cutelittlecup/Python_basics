def fibonacci(number_index: int) -> int:
    """
    Calculate the specified Fibonacci number.

    :param number_index: number that needs to be calculated

    :raises ValueError: if number_index < 0

    :return: result of calculation
    """
    number, last_number = 0, 1
    if number_index == 0:
        return 0
    elif number_index < 0:
        raise ValueError(f"You cannot calc a Fibonacci number from the index {number}")
    for _ in range(number_index - 1):
        number, last_number = last_number, number + last_number
    return last_number


n = int(input('Enter a number: '))

print(f"Fibonacci number by number {n} is {fibonacci(n)}")