"""
year = int(input())
if year % 100:
    print('NO')
else:
    print('YES')

a1, b1, a2, b2 = map(int, (input() for _ in range(4)))
x = y = 0
res = 'NO'
if a1 % 2 and b1 % 2 or not a1 % 2 and not b1 % 2:
    x = 1
if a2 % 2 and b2 % 2 or not a2 % 2 and not b2 % 2:
    y = 1
if x == y:
    res = 'YES'
print(res)

years, gender = int(input()), input()
res = 'NO'
if 10 <= years <= 15 and gender == 'f':
    res = 'YES'
print(res)

print(['ошибка', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X'][next(x if x in range(11) else 0 for x in [int(input())])])

x = int(input())
res = 'NO'
if x % 2:
    res = 'YES'
elif not x % 2 and 6 <= x <= 20:
    res = 'YES'
print(res)

x1, y1, x2, y2 = map(int, (input() for _ in range(4)))
res = 'NO'
if abs(x1 - x2) == abs(y1 - y2):
    res = 'YES'
print(res)

x1, y1, x2, y2 = map(int, (input() for _ in range(4)))
res = 'NO'
if abs((x1 - x2) * (y1 - y2)) == 2:
    res = 'YES'
print(res)
"""
x1, y1, x2, y2 = map(int, (input() for _ in range(4)))
res = 'NO'
if abs(x1 - x2) == abs(y1 - y2) or x1 == x2 or y1 == y2:
    res = 'YES'
print(res)
