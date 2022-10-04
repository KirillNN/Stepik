"""
n, k = map(int, (input(), input()))
print(["YES", "NO", "Don't know"][(n >= k) + (n == k)])

print(['Равносторонний', 'Равнобедренный', 'Разносторонний'][len(set(map(int, (input() for _ in range(3))))) - 1])

x = map(int, (input() for _ in range(3)))
print(sorted(x)[1])

x = int(input())
if x in (1, 3, 5, 7, 8, 10, 12):
    print(31)
elif x == 2:
    print(28)
else:
    print(30)

weight = int(input())
print(["Легкий вес", "Первый полусредний вес", "Полусредний вес"][(weight >= 60) + (weight >= 64) + (weight >= 69)])

a, b, zn = int(input()), int(input()), input()
zn_good = '+-*/'
if zn not in zn_good:
    print('Неверная операция')
elif zn == '/' and b == 0:
    print('На ноль делить нельзя!')
elif zn == '/':
    print(a / b)
elif zn == '*':
    print(a * b)
elif zn == '-':
    print(a - b)
else:
    print(a + b)

color1, color2 = input(), input()
if color1 == 'красный' and color2 == 'синий':
    print('фиолетовый')
elif color2 == 'красный' and color1 == 'синий':
    print('фиолетовый')
elif color1 == 'красный' and color2 == 'желтый':
    print('оранжевый')
elif color2 == 'красный' and color1 == 'желтый':
    print('оранжевый')
elif color1 == 'синий' and color2 == 'желтый':
    print('зеленый')
elif color2 == 'синий' and color1 == 'желтый':
    print('зеленый')
elif color2 == 'красный' and color1 == 'красный':
    print('красный')
elif color2 == 'желтый' and color1 == 'желтый':
    print('желтый')
elif color2 == 'синий' and color1 == 'синий':
    print('синий')
else:
    print('ошибка цвета')

point = int(input())

if point == 0:
    print('зеленый')
elif 1 <= point <= 10 or 19 <= point <= 28:
    if point % 2:
        print('красный')
    else:
        print('черный')
elif 11 <= point <= 18 or 29 <= point <= 36:
    if point % 2:
        print('черный')
    else:
        print('красный')
else:
    print('ошибка ввода')
"""
a1, b1, a2, b2 = map(int, (input() for _ in range(4)))
across = set(range(a1, b1 + 1)) & set(range(a2, b2 + 1))
if len(across) == 0:
    print('пустое множество')
elif len(across) == 1:
    print(*across)
else:
    print(min(across), max(across))
