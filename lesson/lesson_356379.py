'''
# step 11
import random

n = int(input())  # количество попыток
for _ in range(n):
    print(random.choice(['Орел', 'Решка']))

# step 12
import random

n = int(input())  # количество попыток
for _ in range(n):
    print(random.randint(1, 6))

# step 13
import random

length = int(input())  # длина пароля
for _ in range(length):
    print(random.choice([chr(random.randint(65, 90)), chr(random.randint(97, 122))]), end='')
'''
# step 14
import random

numbers = set()
while len(numbers) < 7:
    numbers.add(random.randint(1, 49))

numbers = sorted(list(numbers))
print(*numbers)
