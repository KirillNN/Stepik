# summ_all=0
# for i in range(1000, 10000):
#     summ = 0
#     x=i
#     while i:
#         summ += i % 10
#         i //= 10
#     if summ == 20:
#         summ_all += x
# print(summ_all)

# user_number = int(input())
#
# for line in range(user_number + 1):
#     for number in range(line):
#         print(number+1, end=' ')
#     print()

# n = int(input())
# count = 0
#
# for i in range(n + 1, n * 2):
#     k = 0
#     for j in range(2, int(i ** 0.5)+1):  # определяем простое число или нет
#         if i % j == 0:
#             k += 1
#             break
#     if not k:
#         count += 1
#
# print(count)

# numbers = map(int, input().split())
#
# for number in numbers:
#     print('*' * number)

# n = int(input())
# numbers = list(map(int, input().split()))
# count = 0
# count_new = 0
# while True:
#     for i in range(n - 1):
#         if numbers[i] > numbers[i + 1]:
#             numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
#             count += 1
#     if count > count_new:
#         count_new = count
#     else:
#         break
# print(*numbers)
# print(count)


# n = 6
# numbers = list(map(int, '5 4 2 15 6 6'.split()))
n = int(input())
numbers = list(map(int, input().split()))

for i in range(1, n):
    for j in range(i - 1, -1, -1):
        if numbers[i] < numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]
            i -= 1
        else:
            break
print(*numbers)
