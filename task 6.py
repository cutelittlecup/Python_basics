def fibonacci(number_index):
    number, last_number = 0, 1
    if number_index == 0:
        return 0
    for _ in range(number_index - 1):
        number, last_number = last_number, number + last_number
    return last_number


n = int(input('Enter a number: '))

print(f"Fibonacci number by number {n} is {fibonacci(n)}")
