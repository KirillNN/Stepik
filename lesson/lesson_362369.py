'''
# step 6
from fractions import Fraction

numbers = ['6.34', '4.08', '3.04', '7.49', '4.45', '5.39', '7.82', '2.76', '0.71', '1.97', '2.54', '3.67', '0.14',
           '4.29', '1.84', '4.07', '7.26', '9.37', '8.11', '4.30', '7.16', '2.46', '1.27', '0.29', '5.12', '4.02',
           '6.95', '1.62', '2.26', '0.45', '6.91', '7.39', '0.52', '1.88', '8.38', '0.75', '0.32', '4.81', '3.31',
           '4.63', '7.84', '2.25', '1.10', '3.35', '2.05', '7.87', '2.40', '1.20', '2.58', '2.46']

print(*[f'{x} = {y}' for x, y in list(zip(numbers, map(Fraction, numbers)))], sep='\n')

# step 7
from fractions import Fraction

s = '0.78 4.3 9.6 3.88 7.08 5.88 0.23 4.65 2.79 0.90 4.23 2.15 3.24 8.57 0.10 8.57 1.49 5.64 3.63 8.36 1.56 6.67 1.46 5.26 4.83 7.13 1.22 1.02 7.82 9.97 5.40 9.79 9.82 2.78 2.96 0.07 1.72 7.24 7.84 9.23 1.71 6.24 5.78 5.37 0.03 9.60 8.86 2.73 5.83 6.50 0.123 0.00021'.split()

print(Fraction(min(map(Fraction, s)) + max(map(Fraction, s))))

# step 8
from fractions import Fraction as F

print(F(f'{input()}/{input()}'))

# step 9
from fractions import Fraction as F

a = input()
b = input()

print(f'{a} + {b} = {F(a) + F(b)}')
print(f'{a} - {b} = {F(a) - F(b)}')
print(f'{a} * {b} = {F(a) * F(b)}')
print(f'{a} / {b} = {F(a) / F(b)}')

# step 10
from fractions import Fraction as F

print(F(sum([F(1, (x + 1) ** 2) for x in range(int(input()))])))

# step 11
from fractions import Fraction as F
from math import factorial

print(F(sum([F(1, factorial(x + 1)) for x in range(int(input()))])))

# step 12
from fractions import Fraction as F
from math import gcd

n = int(input())
numerator = n // 2
denominator = n - numerator
while gcd(numerator, denominator) != 1:
    numerator -= 1
    denominator += 1
print(F(numerator, denominator))
'''
# step 13
from fractions import Fraction as F

n = int(input())
result = []
for i in range(1, n):
    for j in range(2, n + 1):
        frac = F(i, j)
        if frac < 1 and frac not in result:
            result.append(frac)

print(*sorted(result), sep='\n')
