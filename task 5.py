import random

f = open('text.txt', 'w')
for i in range(10):
    x = random.randint(-100, 100)
    f.write(str(x) + '\n')
f.close()

j = 0
k = 0
array = []

f = open('text.txt', 'r')

for row in f:
    row = int(row)
    if (row % 2) == 0:
        j += 1
    else:
        k += 1
    array.append(row)

print(f"Max number: {max(array)}")
print(f"Min number: {min(array)}")
print(f"Number of even: {j}")
print(f"Number of odd: {k}")
