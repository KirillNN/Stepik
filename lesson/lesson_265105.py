"""
a, b = map(float, (input() for _ in range(2)))
print(a * b / 2)

s, v1, v2 = map(float, (input() for _ in range(3)))
print(s / (v1 + v2))

x = float(input())
print(1 / x if x else 'Обратного числа не существует')

x = float(input())
print((x - 32) * 5 / 9)

x = int(input())
if x < 3:
    print(x * 10.5)
else:
    print(21 + (x - 2) * 4)

x = float(input())
print(int(x * 10) % 10)

x = float(input())
print(x - int(x))

s = list(map(int, (input() for _ in range(5))))
print(f'Наименьшее число = {min(s)}')
print(f'Наибольшее число = {max(s)}')

s = map(int, (input() for _ in range(3)))
print(*sorted(s, reverse=True), sep='\n')

x = list(map(int, sorted(input())))
res = 'Число неинтересное'
if x[2] - x[0] == x[1]:
    res = 'Число интересное'
print(res)

print(sum(map(abs, map(float, (input() for _ in range(5))))))
"""
p1, p2, q1, q2 = map(int, (input() for _ in range(4)))
print(abs(p1 - q1) + abs(p2 - q2))
