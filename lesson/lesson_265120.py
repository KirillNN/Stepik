"""
m, n = map(int, (input() for _ in range(2)))
for i in range(m, n + 1):
    print(i)

m, n = map(int, (input() for _ in range(2)))
if m <= n:
    for i in range(m, n + 1):
        print(i)
else:
    for i in range(m, n - 1, -1):
        print(i)

m, n = map(int, (input() for _ in range(2)))
for i in range(m, n - 1, -1):
    if i % 2:
        print(i)

m, n = map(int, (input() for _ in range(2)))
for i in range(m, n + 1):
    if not i % 17 or i % 10 == 9 or not (i % 3 or i % 5):
        print(i)
"""
n = int(input())
for i in range(1, 11):
    print(f'{n} x {i} = {n * i}')
