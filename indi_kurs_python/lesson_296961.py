# n = int(input())
# list_n = []
# for _ in range(n):
#     list_n.append(input())
# print(list_n)


# letter = input()
# words = input().split()
#
# for word in words:
#     if word.lower().find(letter) != -1:
#         print(word)

# numbers = [x for x in map(int, input().split()) if x > 0]
# min_pos = 'Empty'
# if numbers:
#     min_pos = min(numbers)
# print(min_pos)

# word = input().lower()
# count = dict()
# for letter in word:
#     x = count.get(letter)
#     if x:
#         count[letter] += 1
#     else:
#         count[letter] = 1
# print(max(count.values()))

# word = input()
# count = 0
# summ = 0
# for letter in word:
#     if letter.isdigit():
#         count += 1
#         summ += int(letter)
# print(count, summ)

# psp = input()
# for i in range(len(psp)):
#     psp = psp.replace('()', '')
#     psp = psp.replace('[]', '')
#     psp = psp.replace('{}', '')
#     if not psp:
#         print('YES')
#         break
# else:
#     print('NO')

# number = int(input())
# count = [0] * 10
#
# while number:
#     count[number % 10] += 1
#     number //= 10
#
# for i, v in enumerate(count):
#     if v:
#         print(i, v)

# n = int(input())
# numbers = map(int, input().split())
# count = [0] * 201
# for number in numbers:
#     count[number + 100] += 1
# result = []
# for i, v in enumerate(count):
#     if v:
#         result.extend([i - 100] * v)
# print(*result)

