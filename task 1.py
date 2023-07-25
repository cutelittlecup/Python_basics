import random

array = random.sample(range(1000), 10)
print('Without sorting:', array)

i = 0
n = 0
while i < len(array) * (len(array) - 1) / 2:
    if n + 1 < len(array):
        if array[n] > array[n + 1]:
            array[n], array[n + 1] = array[n + 1], array[n]
    n += 1
    if n + 1 >= len(array):
        i -= 1
        n = 0
    i += 1

print('With sorting:', array)
