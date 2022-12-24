# step 1
# n = int(input())
#
# total = 0
# for line in range(1, n + 1):
#     for number in range(line):
#         total += 1
#         print(total, end=' ')
#     print()

# step 2
# n = int(input())
# # n = 3
# total = 1
# for i in range(n):
#     for j in range(i):
#         print(total + j, end='')
#     print(i + 1, end='')
#     for j in range(i, 0, -1):
#         print(j + total - 1, end='')
#     print()

# step 3
# a, b = int(input()), int(input())
#
# max_sum = 0
# max_number = 0
# for i in range(a, b + 1):
#     new_sum = 0
#     for j in range(1, i + 1):
#         if i % j == 0:
#             new_sum += j
#     if new_sum >= max_sum:
#         max_sum = new_sum
#         max_number = i
# print(max_number, max_sum)

# step 4
# n = int(input())
#
# for i in range(1, n + 1):
#     print(i, end='')
#     for j in range(1, i + 1):
#         if i % j == 0:
#             print('+', end='')
#     print()

# step 5
# n = int(input())
#
# sum_digit = 0
# while n > 0:
#     sum_digit += n % 10
#     n //= 10
#     if not n and sum_digit > 10:
#         n = sum_digit
#         sum_digit = 0
#
# print(sum_digit)

# step 6
# n = int(input())
# partial_factorial = 1
# partial_sum = 0
# for i in range(1, n + 1):
#     partial_factorial *= i
#     partial_sum += partial_factorial
# print(partial_sum)

# step 7
a, b = int(input()), int(input())

if a <= 2:
    lst = [2]
else:
    lst = []
for i in range(max(3, (a // 2) * 2 + 1), b + 1, 2):
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            break
    else:
        lst.append(i)

print('\n'.join(map(str, lst)))
