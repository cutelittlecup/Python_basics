def fibonacci(number_index):
    number, last_number = 1, 0
    for _ in range(number_index - 1):
        new_number = number + last_number
        number, last_number = new_number, number
    return number


n = int(input('Enter a number: '))

print(f"Fibonacci number by number {n} is {fibonacci(n)}")
