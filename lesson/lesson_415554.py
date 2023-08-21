# step 1
# n = int(input())
# first, second, third, four = 0, 0, 0, 0
# for i in range(n):
#     x, y = map(int, input().split())
#     if x > 0 and y > 0:
#         first += 1
#     elif x < 0 < y:
#         second += 1
#     elif x < 0 and y < 0:
#         third += 1
#     elif x > 0 > y:
#         four += 1
#
# print(f'Первая четверть: {first}')
# print(f'Вторая четверть: {second}')
# print(f'Третья четверть: {third}')
# print(f'Четвертая четверть: {four}')

# step 2
# numbers = list(map(int, input().split()))
# count = 0
# for x, y in zip(numbers, numbers[1:]):
#     if x < y:
#         count += 1
#
# print(count)


# step 3
# numbers = input().split()
# result = []
# for x, y in zip(numbers[::2], numbers[1::2]):
#     result.extend([y, x])
# if len(numbers) % 2:
#     result.append(numbers[-1])
# print(*result)

# step 4
# numbers = input().split()
# result = [numbers[-1]] + numbers[:-1]
# print(*result)

# step 5
numbers = list(map(int, input().split()))
count = 0
for x, y in zip(numbers, numbers[1:]):
    if x < y:
        count += 1

print(count + 1)

# step 6
n = int(input())
numbers = []
for _ in range(n):
    numbers.append(int(input()))
multi = int(input())
result = "НЕТ"
for i, x in enumerate(numbers):
    for j, y in enumerate(numbers):
        if i != j and x * y == multi:
            result = "ДА"
            break
print(result)

# step 7
tim = input()
rus = input()
if tim == rus:
    print('ничья')
elif tim == 'камень' and rus == 'ножницы':
    print('Тимур')
elif tim == 'ножницы' and rus == 'бумага':
    print('Тимур')
elif tim == 'бумага' and rus == 'камень':
    print('Тимур')
else:
    print('Руслан')

# step 7
tim = input().lower()
rus = input().lower()

win_words = [
    "камень-ножницы",
    "камень-ящерица",
    "ножницы-бумага",
    "ножницы-ящерица",
    "бумага-камень",
    "бумага-спок",
    "ящерица-бумага",
    "ящерица-спок",
    "спок-ножницы",
    "спок-камень"
]

if tim == rus:
    print('ничья')
elif tim + '-' + rus in win_words:
    print('Тимур')
else:
    print('Руслан')
