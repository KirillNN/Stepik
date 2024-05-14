'''
# step 6
import random

n = 10 ** 6
k = 0
s0 = 16
for _ in range(n):
    x = random.uniform(-2, 2)
    y = random.uniform(-2, 2)

    if x ** 3 + y ** 4 + 2 >= 0 and 3 * x + y ** 2 <= 2:  # если попадает в нужную область
        k += 1

print((k / n) * s0)
'''
# step 8
import random

n = 10 ** 6
k = 0
s0 = 4
for _ in range(n):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x ** 2 + y ** 2 <= 1:  # если попадает в нужную область
        k += 1

print((k / n) * s0)
