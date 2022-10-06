"""
for _ in range(10):
    print('Python is awesome!')

text = input()
n = int(input())
for _ in range(n):
    print(text)

n = int(input())
for _ in range(n):
    print('*' * 19)

text = input()
for i in range(10):
    print(f'{i} {text}')

n = int(input())
for i in range(n + 1):
    print(f'Квадрат числа {i} равен {i ** 2}')

n = int(input())
for i in range(n, 0, -1):
    print('*' * i)
"""
m, p, n = map(int, (input() for _ in range(3)))
for i in range(1, n + 1):
    print(f'{i} {m}')
    m *= (1 + p / 100)
