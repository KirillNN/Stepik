"""
# step 6
numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2,
           12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]
print(len(numbers))
print(numbers[-1])
print(numbers[::-1])
print('YES') if all(x in [5, 17] for x in numbers) else print('NO')
del numbers[0]
del numbers[-1]
print(numbers)

# step 7
n = int(input())
numbers = []
for _ in range(n):
    numbers.append(input())

print(numbers)

# step 8
from string import ascii_lowercase

s = list(ascii_lowercase)
numbers = []
for i, c in enumerate(s):
    numbers.append(c * (i + 1))

print(numbers)

# step 9
n = int(input())
numbers = []
for _ in range(n):
    numbers.append(int(input()) ** 3)

print(numbers)

# step 10
n = int(input())
numbers = []
for i in range(1, n + 1):
    if not n % i:
        numbers.append(i)

print(numbers)

# step 11
numbers = []
for _ in range(int(input())):
    numbers.append(int(input()))
print([x + y for x, y in zip(numbers, numbers[1:])])

# step 12
numbers = []
for _ in range(int(input())):
    numbers.append(int(input()))

print(numbers[::2])

# step 13
numbers = []
for _ in range(int(input())):
    numbers.append(input())
k = int(input())
result = ''
for word in numbers:
    if len(word) >= k:
        result += word[k - 1]
print(result)
"""
# step 14
words = []
for _ in range(int(input())):
    words.extend(input())
print(words)
