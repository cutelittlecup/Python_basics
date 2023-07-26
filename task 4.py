def calculator(num1, op, num2):
    operations = {'mod': '%', 'pow': '**', 'div': '//'}
    try:
        if op in operations:
            result = eval(f'{num1} {operations[op]} {num2}')
        else:
            result = eval(f'{num1} {op} {num2}')
    except ZeroDivisionError:
        result = "infinity"
    return result


num1 = input('Enter the first number: ')
op = str(input('Enter the operation: '))
num2 = input('Enter the second number: ')

print(f'Result: {num1} {op} {num2} = {calculator(num1, op, num2)}')
