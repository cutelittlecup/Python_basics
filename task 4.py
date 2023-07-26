def calculator(number1, operation, number2):
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

print(f'Result: {num1} {op} {num2} = {calculator(num1, op, num2)}')
