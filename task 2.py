def fact(n, a):
    a = a * n
    if n > 1:
        return fact(n - 1, a)
    else:
        return a


n = int(input('Enter a number: '))

print('Result:', fact(n, 1))
