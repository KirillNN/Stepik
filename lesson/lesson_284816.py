"""
a = 15 // (16 % 7)
b = 34 % a * 5 - 29 % 5 * 2
print(a + b)
a = 82 // 3 ** 2 % 7
print(a)

b1, q, n = map(int, (input(), input(), input()))
print(b1 * q ** (n - 1))

print(int(input()) // 100)

a, b = map(int, (input(), input()))
print(b // a)
print(b % a)

print((int(input()) + 1) // 2)

print(1 + ((int(input()) - 1) // 4))

time = int(input())
print(f'{time} мин - это {time // 60} час {time % 60} минут.')

x = int(input())
summ = 0
multi = 1
while x:
    summ += x % 10
    multi *= x % 10
    x //= 10
print(f'Сумма цифр = {summ}')
print(f'Произведение цифр = {multi}')

a, b, c = input()
print(a, b, c, sep='')
print(a, c, b, sep='')
print(b, a, c, sep='')
print(b, c, a, sep='')
print(c, a, b, sep='')
print(c, b, a, sep='')

x = int(input())
ar = []
while x:
    ar.append(x % 10)
    x //= 10
print(f'Цифра в позиции тысяч равна {ar[3]}')
print(f'Цифра в позиции сотен равна {ar[2]}')
print(f'Цифра в позиции десятков равна {ar[1]}')
print(f'Цифра в позиции единиц равна {ar[0]}')
"""
n = 12345
print(n % 1000 // 100)
