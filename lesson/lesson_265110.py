"""
import math

num1 = math.sqrt(2)     # вычисление корня квадратного из двух
num2 = math.ceil(3.8)   # округление числа вверх
num3 = math.floor(3.8)  # округление числа вниз

print(num1)
print(num2)
print(num3)

x1, y1, x2, y2 = map(float, (input() for _ in range(4)))
print(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5)

from math import pi

r = float(input())
print(pi * r ** 2)
print(2 * pi * r)

a, b = map(float, (input() for _ in range(2)))
print((a + b) / 2)
print((a * b) ** 0.5)
print(2 * a * b / (a + b))
print(((a ** 2 + b ** 2) / 2) ** 0.5)

from math import pi, sin, cos, tan

x = float(input())
r = x * pi / 180
print(sin(r) + cos(r) + tan(r) ** 2)

from math import ceil, floor

x = float(input())
print(ceil(x) + floor(x))

import math

a = float(input())
b = float(input())
c = float(input())

di = b ** 2 - 4 * a * c
if di > 0:
    x1 = (-b + math.sqrt(di)) / (2 * a)
    x2 = (-b - math.sqrt(di)) / (2 * a)
    if x1 < x2:
        print(x1, x2, sep='\n')
    else:
        print(x2, x1, sep='\n')
elif di == 0:
    x = -b / (2 * a)
    print(x)
else:
    print('Нет корней')
"""
from math import pi, tan

n = int(input())
a = float(input())

print(n * a ** 2 / (4 * tan(pi / n)))
