# n = int(input())
# for i in range(n):
#     word = input().lower()
#     x = word.find('рок')
#     if x != -1:
#         print(i + 1, x + 1)
#
# n = int(input())
# result = []
# for i in range(n):
#     word = input()
#     x = word.find('соль')
#     if x == -1:
#         result.append(word)
# print(', '.join(result))

# n = int(input())
# summ = 0
# for i in range(1, n):
#     if i % 3 == 0 or i % 5 == 0:
#         summ += i
# print(summ)

summ = 0
for i in range(50,101):
    summ += i**3
print(summ)