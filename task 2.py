def fact(number, a):
    a = a * number
    if number > 1:
        return fact(number - 1, a)
    else:
        return a


n = int(input('Enter a number: '))

print(f'Result: {fact(n, 1)}')
