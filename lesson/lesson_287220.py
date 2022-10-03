"""
a = 17 // (23 % 7)
b = 34 % a * 5 - 29 % 4 * 3
print(a * b)

print('*****************')
print('*               *')
print('*               *')
print('*****************')

a, b = map(int, (input(), input()))
print(f'Квадрат суммы {a} и {b} равен {(a + b) ** 2}')
print(f'Сумма квадратов {a} и {b} равна {a ** 2 + b ** 2}')

a, b, c, d = map(int, (input(), input(), input(), input()))
print(a ** b + c ** d)
"""
x = input()
print(int(x) + int(x * 2) + int(x * 3))
