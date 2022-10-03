"""
s = 0
k = 30
d = k - 5
k = 2 * d
s = k - 100
print(s)

x = 3
y = 4
z = x + y
z = z + 1
x = y
y = 5
x = z + y + 7
print(x)

x = int(input())
print(x, x + 1, x + 2, sep='\n')

x = map(int, (input(), input(), input()))
print(sum(x))

a = int(input())
print(f'Объем = {a ** 3}')
print(f'Площадь полной поверхности = {6 * a ** 2}')

a, b = map(int, (input(), input()))
print(3 * (a + b) ** 3 + 275 * b ** 2 - 127 * a - 41)

x = int(input())
print(f'Следующее за числом {x} число: {x + 1}')
print(f'Для числа {x} предыдущее число: {x - 1}')

a, b, c, d = map(int, (input(), input(), input(), input()))
print((a + b + c + d) * 3)

a, b = map(int, (input(), input()))
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')

a1, d, n = map(int, (input(), input(), input()))
print(a1 + d * (n - 1))
"""
x = int(input())
print(*[i * x for i in range(1, 6)], sep='---')
