"""
a, b = input(), input()
if a == b:
    print('Пароль принят')
else:
    print('Пароль не принят')

x = int(input())
if x % 2:
    print('Нечетное')
else:
    print('Четное')

a, b, c, d = map(int, input())
print('ДА') if a + d == b - c else print('НЕТ')

print('Доступ запрещен') if int(input()) < 18 else print('Доступ разрешен')

a, b, c = map(int, (input(), input(), input()))
print('YES') if b - a == c - b else print('NO')

print(min(map(int, (input(), input()))))

print(min(map(int, (input() for _ in range(4)))))

x = int(input())
print(['детство', 'молодость', 'зрелость', 'старость'][(x > 13) + (x > 24) + (x > 59)])
"""
print(sum(x for x in map(int, (input() for _ in range(3))) if x > 0))
