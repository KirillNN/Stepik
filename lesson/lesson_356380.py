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
'''
# step 10
from random import shuffle

word = list(input())
shuffle(word)
print(*word, sep='')
