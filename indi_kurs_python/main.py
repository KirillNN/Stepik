# ticker, y, z = map(int, input().split())
# print(ticker * 3 + y * 5 + z * 12)

# n, a, b = map(int, input().split())
# print(n * a * b * 2)

# print((lambda n, a, b: 2 * n * a * b)(*list(map(int, input().split()))))

# ticker = list(map(int, input().split()))
# print(sum(ticker) / len(ticker))

# ticker = []
# y = []
# for _ in range(3):
#     ticker.append(int(input()))
#
# for _ in range(3):
#     y.append(int(input()))
#
# hour = (y[0] - ticker[0]) * 3600
# min = (y[1] - ticker[1]) * 60
# sec = y[2] - ticker[2]
# print(hour + min + sec)

# ticker, y = map(int, input().split())
# print(*[y - 1, ticker - 1])

# ticker = []
# for _ in range(2):
#     ticker.append(abs(int(input())))
#
# print(sum(ticker))
#
# print(sum(abs(int(input())) for _ in 'ab'))

# a, b = map(float, input().split())
# print(max(a, b) - min(a, b))

# print(max(map(int, input().split())))

# a = int(input())
# b = int(input())
# c = int(input())
# print(max(a + b * c, a * (b + c), a * b * c, (a + b) * c, a + b + c))

# a = float(input())
# print(round(a, 2), round(a, 3))

# print(*input().split(), sep=',')

# ticker = int(input())
# print(ticker - 1, '<', ticker, '<', ticker + 1, sep='')

# print(*[input() for _ in range(3)], sep='---')

# print(*range(1, 6), sep=input())

# print(input(), end=' - Сказала она!')

# print('Гвидо', 'Ван', 'Россум', sep='*', end='-')
# print('Основатель', 'Питона', sep='_', end='!')

# print(int(input()) // 1000)

# a, b = (int(input()) for _ in range(2))
# print(a // b)

# print(int(input()) % 10)
# print(int(input()) // 100 % 10) # выводит разряд сотен

# ticker = int(input())
# a = ticker % 10
# b = ticker // 10 % 10
# c = ticker // 100
# print(a + b + c)

# ticker = int(input())
# count = 0
# count += ticker // 100
# ticker -= ticker // 100 * 100
# count += ticker // 20
# ticker -= ticker // 20 * 20
# count += ticker // 10
# ticker -= ticker // 10 * 10
# count += ticker // 5
# ticker -= ticker // 5 * 5
# count += ticker
# print(count)

# ticker = int(input())
# ticker %= 60 * 24
# print(ticker // 60, ticker % 60)

# ticker = int(input())
# print(2 * (ticker // 2 + 1))

# ticker = int(input())
# hour = ticker // 3600
# minute = (ticker - hour * 3600) // 60
# sec = ticker - hour * 3600 - minute * 60
# print(f'{hour}:{minute:02}:{sec:02}')

# print(int(input()) % 2 == 0)
# print(not int(input()) % 2)
# print(not int(input()) % 6)
# print(not not int(input()) % 9)
# print(bool(int(input()) % 9))
# print(int(input()) % 10 == 2)
#
# ticker, y = map(int, input().split())
# print(not (ticker % 7) and not (y % 7))
#
# ticker, y, z = map(int, input().split())
# print(ticker == y == z)
#
# print(5 < int(input()) <= 19)
#
# print('awesome' in (input() for _ in range(2)))

# a, b, c = input().split()
# print(a == b or a == c or b == c)
#
# print(len(input()) == 2)
# print(9 < int(input()) < 100)
# print(int(input()) in range(10, 100))
#
# ticker, y, z = map(int, input().split())
# print(max(ticker, y, z) ** 2 == (ticker ** 2 + y ** 2 + z ** 2) - max(ticker, y, z) ** 2)

# from math import ceil
#
# ticker, y, z = map(int, input().split())
# print(ceil((ticker + y) * z / 8))
# print(ceil(int(input()) / 4))

# ticker, y, z = (int(input()) for _ in range(3))
# print(ceil(ticker / 2) + ceil(y / 2) + ceil(z / 2))
# a = 'Я стану крутым программистом!'
# print(a, a, a, sep='\n')
#
# print("""Что Вы сказали? {0}? Какое интересное слово""".format(input()))
#
# name = input()
# surname = input()
# print("Здравствуйте, {1} {0}!".format(name, surname))
#
# print("Здравствуйте, {1} {0}!".format(input(), input()))
#
# ticker = int(input())
# print('Для числа {0} предыдущим будет число {1}.'.format(ticker, ticker - 1))
# print('Для числа {0} следующим будет число {1}.'.format(ticker, ticker + 1))
#
# print(f'Мое имя {input()}!')
#
# name, age = (input() for _ in range(2))
# print(f'Hello {name.upper()}. You are {age} years old.')
#
# name, year = (input() for _ in range(2))
# print(f'{name}, вам исполнится 77 лет в {int(year) + 77}')
#
# ticker = int(input())
# print(f"{ticker} сек - это {ticker // 60} мин. {ticker % 60} сек.")
#
# ticker, y = map(int, input().split())
# print(f"Разрешение экрана: {ticker} ticker {y}.\nОбщее количество пикселей = {ticker * y}.")
#
# ticker, y = (int(input()) for _ in range(2))
# print(f'{ticker} / {y} = {ticker / y}\n{ticker} // {y} = {ticker // y}\n{ticker} % {y} = {ticker % y}')
#
# ticker, y, z = (int(input()) for _ in range(3))
# print(f'Vector A({ticker}, {y}, {z})\nVector B({ticker + 5}, {y + 5}, {z + 5})')
#
# ticker, y = (input() for _ in range(2))
# print(f'Current dollar rate is {ticker}. You want buy {y} dollars\nYou must pay {float(ticker) * int(y)}')
#
# my_list = list(map(int, input().split()))
# print(777 in my_list)
#
# list_numbers = list(map(int, input().split()))
# print(sum(list_numbers))
#
# mas = list(map(int, input().split()))
# print(min(mas), max(mas))
#
# list_numbers = list(map(int, input().split()))
# print(sum(list_numbers) / len(list_numbers))
#
# a = list(map(int, input().split()))
# print(a[1])
#
# a = list(map(int, input().split()))
# print(a[2:5])
#
# a = list(map(int, input().split()))
# print(a[-3:])
#
# a = list(map(int, input().split()))
# print(a[1::3])
#
# a = list(map(int, input().split()))
# print(a[::-1])

# a = list(map(int, input().split()))
# print(a.count(999))

# ticker, y = input().upper().split()
# print(*ticker, sep='-', end=' ')
# print(*y, sep='-')
#
# print('\n'.join(input().split()))
#
# ticker, y, z = input().split()
# print(f'{z} {ticker[0]}.{y[0]}.')
#
# ticker = int(input())
# print(ticker if ticker < 20000 else ticker * 0.87)
#
# print('ДА' if input() == 'Python' else 'НЕТ')
#
# ticker = (int(input()) for _ in range(2))
# print(max(ticker))
#
# ticker = input()
# print('YES' if ticker == ticker[::-1] else 'NO')
#
# a, b, c = map(int, input().split())
# print('YES' if a + b == c else 'NO')
#
# word1, word2 = (input() for _ in range(2))
# print('YES' if word1 == word2[::-1] else 'NO')
#
# a, b, c = (int(input()) for _ in range(3))
# print('YES' if a + b > c and a + c > b and b + c > a else 'NO')

# ticket = input().zfill(6)
# middle = len(ticket) // 2
# left = sum(map(int, ticket[:middle]))
# right = sum(map(int, ticket[middle:]))
# print('YES' if left == right else 'NO')

# a, b = (input() for _ in range(2))
# one, two = ord(a[0]) + int(a[1]), ord(b[0]) + int(b[1])
# print('YES' if (one ^ two) % 2 == 0 else 'NO')
#
# n = int(input())
# print([int(n / 2), -int((n + 1) / 2)][n % 2])
#
# a, b = (int(input()) for _ in range(2))
# if a < b:
#     print('<')
# elif a > b:
#     print('>')
# else:
#     print('=')
# print(['<', '>', '='][(a >= b) + (a == b)])
#
# a, b, c = (int(input()) for _ in range(3))
# if b > a:
#     a = b
# if c > a:
#     a = c
# print(a)

# n = int(input())
# print([n // 2, n, 0][(n % 2) + (n == 1)])

# a, b, c = map(int, input().split())
# if a > b:
#     a, b = b, a
# if b > c:
#     b, c = c, b
# if a > b:
#     a, b = b, a
# print(c - a)
#
# s, v1, v2, t1, t2 = map(int, input().split())
# x = t1 * 2 + v1 * s
# y = t2 * 2 + v2 * s
# print(['First', 'Second', 'Friendship'][(x >= y) + (x == y)])

# letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
# for letter in letters:
#     print(letter, ord(letter))

# a, b = (input().lower() for _ in range(2))
# if a[-1] == 'ь':
#     print('Good' if a[-2] == b[0] else 'Bad')
# else:
#     print('Good' if a[-1] == b[0] else 'Bad')

# n = int(input())
# print([n, 'Buzz', 'Fizz', 'FizzBuzz'][(n % 3 == 0) * 2 + (n % 5 == 0)])

# num_1, num_2, num_3 = (int(input()) for _ in range(3))
# if num_1 == num_2 and num_1 == num_3:
#     print(3)
# elif num_1 == num_2 or num_1 == num_3 or num_2 == num_3:
#     print(2)
# else:
#     print(0)
#
# n = int(input())
# print(['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь',
#        'Декабрь'][n - 1])

# n = int(input())
# x = ['Младенец', 'Малыш', 'Ребенок', 'Подросток', 'Взрослый человек', 'Пожилой человек']
# y = x[(n >= 2) + (n >= 4) + (n >= 12) + (n >= 19) + (n >= 65)]
# print(y)

# a, b = (float(input()) for _ in range(2))
# op = input()
# if b == 0 or op not in '+-*/':
#     print('Неизвестно')
# elif op == '+':
#     print(a + b)
# elif op == '-':
#     print(a - b)
# elif op == '*':
#     print(a * b)
# else:
#     print(a / b)
#
# a, b = (input() for _ in range(2))
# if len(a) < 7:
#     print('Short')
# elif a != b:
#     print('Difference')
# else:
#     print('OK')

# number = 6785
# while number >= 195:
#     print(number if number % 5 == 0 else '')
#     number -= 5
# numbers = [2, 3, 7, 9, 5, 0, 6, 3, 6, 0, 1, 7, 9, 4, 4, 4, 2, 2, 6, 9, 1, 7, 0, 3, 8, 1, 0, 3, 8, 0, 8, 4, 0, 2, 3, 6,
#            6, 1, 5, 8, 7, 2, 3, 8, 7, 7, 1, 2, 2, 8, 4, 3, 4, 8, 0, 7, 9, 8, 3, 7, 7, 7, 7, 5, 1, 7, 4, 5, 0, 8, 0, 9,
#            2, 4, 7, 6, 6, 5, 9, 7, 1, 7, 8, 8, 3, 4, 9, 7, 6, 4, 2, 0, 0, 0, 9, 4, 0, 9, 4, 4, 4, 5, 5, 4, 2, 5, 9, 4,
#            8, 1, 5, 7, 1, 0, 2, 6, 8, 7, 2, 7, 9, 3, 6, 4, 7, 5, 0, 7, 2, 0, 8, 2, 9, 8, 6, 4, 4, 7, 5, 5, 9, 4, 9, 5,
#            6, 9, 1, 1, 3, 1, 5, 2, 1, 7, 0, 0, 7, 8, 1, 3, 0, 0, 4, 4, 3, 3, 6, 7, 8, 6, 1, 2, 0, 2, 0, 9, 9, 0, 5, 2,
#            4, 1, 7, 4, 9, 9, 4, 9, 6, 9, 2, 7, 1, 2, 4, 5, 4, 0, 9, 0]
# # здесь должен быть ваш код
# while True:
#     if 4 in numbers:
#         numbers.remove(4)
#     else:
#         break
# # здесь должен быть ваш код
# print(*numbers)
#
# word = input()
# while len(word) >= 1:
#     print(word)
#     word = word[1:-1]
#
# n = int(input())
# count = 1
# while n >= count ** 2:
#     print(count ** 2)
#     count += 1

# a, b = map(int, input().split())
# count = 1
# while b > a:
#     a *= 1.15
#     count += 1
# print(count)

# n = int(input())
# result = 'НЕТ'
# pow = 0
# while n >= 2 ** pow:
#     if 2 ** pow == n:
#         result = pow
#     pow += 1
# print(result)

# n = int(input())
# new_n = 0
# while new_n != n and n < 1e9:
#     first_digit = n
#     while first_digit // 10:
#         first_digit //= 10
#     new_n = n
#     n *= first_digit
# print(n)

# result = 0
# n = None
# while n != 0:
#     n = int(input())
#     result += n
# print(result)

# previous = ''
# while True:
#     password = input()
#     if len(password) < 5 or len(password) > 9:
#         print(previous)
#         break
#     previous = password

# volume_max = int(input())
# count = 0
# volume_thing = 0
# while volume_max > 0:
#     thing = int(input())
#     volume_max -= thing
#     if volume_max < 0:
#         break
#     count += 1
#     volume_thing += thing
# print(f'Довольно!\n{volume_thing}\n{count}')
import re

# n, m = map(int, input().split())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
#
# result = []
# index_a = 0
# index_b = 0
# while index_a < n and index_b < m:
#
#     if a[index_a] == b[index_b]:
#         result.append(a[index_a])
#         result.append(b[index_b])
#         index_a += 1
#         index_b += 1
#     elif a[index_a] < b[index_b]:
#         result.append(a[index_a])
#         index_a += 1
#     else:
#         result.append(b[index_b])
#         index_b += 1
#
# if index_a < n:
#     result += a[index_a:]
# if index_b < m:
#     result += b[index_b:]
#
# print(*result)

# n = int(input())
# while n // 10:
#     print(n % 10)
#     n //= 10
# print(n)

# n = int(input())
# summ = 0
# while n // 10:
#     summ += n % 10
#     n //= 10
# summ += n
# print(summ)
#
# n = int(input())
# total = 1
# while n:
#     total *= n % 10
#     n = n // 10
# print(total)
#
# n = int(input())
# mininum = 9
# maximum = 0
# while n:
#     digit = n % 10
#     if digit > maximum:
#         maximum = digit
#     if digit < mininum:
#         mininum = digit
#     n = n // 10
# print(f'{mininum}\n{maximum}')
#
# n = int(input())
# count_7 = 0
# while n:
#     if n % 10 == 7:
#         count_7 += 1
#     n = n // 10
# print(count_7)

# n = int(input())
# while n:
#     print(n % 2)
#     n = n // 2

# n = int(input())
# count = 2
# result = 'Yes'
# while int(n**0.5) > count:
#     if n % count == 0:
#         result = 'No'
#         break
#     count += 1
# print(result)

# my_data = []
# for i in range(2, 1000000):
#     # if i % 100000 == 0:
#     #     print(i)
#     flag = True
#     for divider in range(2, int(i ** 0.5) + 1):
#         if i % divider == 0:
#             flag = False
#             break
#     if flag:
#         my_data.append(i)
# print(*my_data)

# n = int(input())
# divider = 1
# result = 0
# while divider <= n:
#     if n % divider == 0:
#         result += divider
#     divider += 1
# print(result)

# a, b = map(int, input().split())
# while a != 0 and b != 0:
#     if a > b:
#         a = a % b
#     else:
#         b = b % a
# print(a + b)  # НОД
#
# a, b = map(int, input().split())
# a1, b1 = a, b
# while a != 0 and b != 0:
#     if a > b:
#         a = a % b
#     else:
#         b = b % a
# print(int(a1 * b1 / (a + b)))  # НОК

# n = int(input())
# count = 2
# divider = n
# while count <= n:
#     if n % count == 0:
#         divider = count
#         break
#     count += 1
# print(divider)

# a, b = (int(input()) for _ in range(2))
# while a <= b:
#     if a % 2 != 0 and a % 3 != 0:
#         print(a)
#     if a % 777 == 0:
#         break
#     a += 1

# n = int(input())
# count = 0
# while n != 1:
#     n = [3 * n + 1, n // 2][n % 2 == 0]
#     count += 1
# print(count)

# i = 0
# while i < 5:
#     if i == 3:
#         break
#     print(i)
#     i += 1
# else:
#     print("Конец")

# word = input()
# while len(word) > 0:
#     if word[0] in 'ae':
#         print('Ага! Нашлась')
#         break
#     print('Текущая буква:', word[0])
#     word = word[1:]
# else:
#     print('Распечатали все буквы')

# print(list(range(1000, 499,-50)))

# n = int(input())
# for i in range(1, n + 1):
#     print(i)

# n = int(input())
# for i in range(n, 0, -1):
#     print(i)

# phrase = input()
# n = int(input())
# for _ in range(n):
#     print(phrase)

# a, b = (int(input()) for _ in range(2))
# # a, b = 9, 15
# for i in range(a, b + 1):
#     x = [[i, 'Buzz'], ['Fizz', 'FizzBuzz']][i % 3 == 0][i % 5 == 0]
#     print(x)

a, b = (int(input()) for _ in range(2))
for i in range(a, b + 1):
    print(f'Число {i}; его квадрат = {i ** 2}; его куб = {i ** 3}')
