"""
num1 = 34
num2 = 81
if num1 // 9 == 0 or num2 % 9 == 0:
    print('число', num1, 'выиграло')
else:
    print('число', num2, 'выиграло')

a = int(input())
if a >= 2 and a <= 17:
    b = 3
    p = a * a + b * b
else:
    b = 5
p = (a + b) * (a + b)
print(p)

x = int(input())
if -1 < x < 17:
    print('Принадлежит')
else:
    print('Не принадлежит')

x = int(input())
if x <= -3 or x >= 7:
    print('Принадлежит')
else:
    print('Не принадлежит')

x = int(input())
if -30 < x <= -2 or 7 < x <= 25:
    print('Принадлежит')
else:
    print('Не принадлежит')

x = int(input())
if 999 < x < 10000 and (not x % 7 or not x % 17):
    print('YES')
else:
    print('NO')

a, b, c = map(int, (input(), input(), input()))
if a + b > c and a + c > b and b + c > a:
    print('YES')
else:
    print('NO')

x = int(input())
if not x % 4 and x % 100 or not x % 400:
    print('YES')
else:
    print('NO')

x1, y1, x2, y2 = map(int, (input() for _ in range(4)))
if x1 == x2 or y1 == y2:
    print('YES')
else:
    print('NO')
"""
x1, y1, x2, y2 = map(int, (input() for _ in range(4)))
if abs(x1 - x2) < 2 and abs(y1 - y2) < 2:
    print('YES')
else:
    print('NO')
