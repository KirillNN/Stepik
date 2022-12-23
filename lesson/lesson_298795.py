# counter = 0
# for i in range(99, 102):
#     temp = i
#     while temp > 0:
#         counter += 1
#         temp //= 10
# print(counter)

# step 5
# n = input()
# for _ in range(int(n)):
#     print(f'{n} {n} {n}')

# step 6
# n = int(input())
# for i in range(1, n + 1):
#     print(f'{i} ' * 5)

# step 7
# n = int(input())
# for i in range(1, n + 1):
#     for j in range(1, 10):
#         print(f'{i} + {j} = {i + j}')
#     print()

# step 8
# n = int(input())
# for i in range(n):
#     if i <= n // 2:
#         print('*' * (i + 1))
#     else:
#         print('*' * (n - i))

# step 9
# n = int(input())
#
# for line in range(n + 1):
#     for number in range(line):
#         print(line, end='')
#     print()
#
# step 11
# total = 0
# for x in range(1, 15):
#     for y in range(1, 15):
#         for z in range(1, 15):
#             if x * 28 + 30 * y + 31 * z == 365:
#                 total += 1
#                 print('x =', x, 'y =', y, 'z =', z)
# print('Общее количество натуральных решений =', total)

# step 12
total = 0
for x in range(1, 11):
    for y in range(1, 21):
        for z in range(1, 201):
            if x * 10 + y * 5 + z * 0.5 == 100:
                total += 1
                print('x =', x, 'y =', y, 'z =', z)
print('Общее количество натуральных решений =', total)
