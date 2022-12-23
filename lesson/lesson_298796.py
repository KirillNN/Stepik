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
a, b = int(input()), int(input())

max_sum = 0
for i in range(a, b+1):
    for j in range(i, i+1):
        print(j)