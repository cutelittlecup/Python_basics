def calculator(operation: str, number1: str, number2: str) -> float:
    """
    Simple implementation of the functionality of the calculator.

    :param operation: the operation between two numbers
    :param number1: the first number to produce the operation
    :param number2: the second number to produce the operation
    :return: result of the calculation
    """
    operations = {'mod': '%', 'pow': '**', 'div': '//'}
    try:
        if op in operations:
            result = eval(f'{number1} {operations[operation]} {number2}')
        else:
            result = eval(f'{number1} {operation} {number2}')
    except ZeroDivisionError:
        result = "infinity"
    return result


num1 = input('Enter the first number: ')
op = str(input('Enter the operation: '))
num2 = input('Enter the second number: ')

print(f'Result: {num1} {op} {num2} = {calculator(op, num1, num2)}')
