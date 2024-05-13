'''
# step 6
from random import randint as r


def generate_ip():
    ip = []
    for _ in range(4):
        ip.append(r(0, 255))
    return '.'.join(map(str, ip))


# step 7
from random import choice as c
from string import ascii_uppercase


def generate_index():
    result = c(ascii_uppercase) + c(ascii_uppercase)
    result += str(c(range(0, 100)))
    result += '_'
    result += str(c(range(0, 100)))
    result += c(ascii_uppercase) + c(ascii_uppercase)
    return result

# step 8
from random import shuffle

matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]

m1 = [x for y in matrix for x in y]
shuffle(m1)

for i in range(4):
    for y in range(4):
        matrix[i][y] = m1[4 * i + y]

# step 9
from random import randint

result = set()

while len(result) < 100:
    result.add(randint(1000000, 9999999))

print(*result, sep='\n')

# step 10
from random import shuffle

word = list(input())
shuffle(word)
print(*word, sep='')

# step 11
from random import randint

numbers = list()
while len(numbers) < 24:
    x = randint(1, 75)
    if x not in numbers:
        numbers.append(x)
numbers.insert(12, 0)
for i, v in enumerate(numbers):
    if not i % 5:
        print()
    print(str(v).ljust(3), end='')

# step 12
from random import choice

fio = []
for _ in range(int(input())):
    fio.append(input())

fio_used = []
for i in fio:
    pair = choice(fio)
    while pair == i or pair in fio_used:
        pair = choice(fio)
    fio_used.append(pair)
    print(f'{i} - {pair}')

# step 13
from string import ascii_letters, digits
from random import choices

symbols = ascii_letters + digits
symbols_not_used = 'lI1oO0'
# Программа должна вывести "n" паролей длиной "m" символов
n = int(input())
m = int(input())
while n > 0:
    password = choices(symbols, k=m)
    if not any([x in symbols_not_used for x in password]):
        print(*password, sep='')
        n -= 1

# step 14
from string import ascii_letters, digits
from random import choices


def check_complication(data: list, symbols_not_used: str) -> bool:
    check_upper = any([x.isupper() for x in data])
    check_lower = any([x.islower() for x in data])
    check_digit = any([x.isdigit() for x in data])
    check_not_used = not any([x in symbols_not_used for x in data])
    tmp = [x for x in data]
    tmp1 = [x.islower() for x in data]
    tmp2 = [x.isupper() for x in data]
    tmp3 = [x.isdigit() for x in data]
    tmp4 = [x in symbols_not_used for x in data]
    result = all((check_upper, check_lower, check_digit, check_not_used))
    return result


symbols = ascii_letters + digits
symbols_not_used = 'lI1oO0'
# Программа должна вывести "n" паролей длиной "m" символов
# n = int(input())
# m = int(input())
n = 9
m = 7
while n > 0:
    password = choices(symbols, k=m)
    if check_complication(password, symbols_not_used):
        print(*password, sep='')
        n -= 1
#     if not any([x in symbols_not_used for x in password]):
#         print(*password, sep='')
#         n -= 1


# print(check_complication('sdf'))
'''
# step 15

for i in range(48):
    # print(round(i*1.27,2))
    print(i+1)