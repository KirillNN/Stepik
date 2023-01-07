"""
# step 2
numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
print(sum([x * x for x in numbers]))

# step 3
numbers = []
for _ in range(int(input())):
    numbers.append(int(input()))
print(*numbers, sep='\n')
print()
numbers = map(lambda x: x ** 2 + 2 * x + 1, numbers)
print(*numbers, sep='\n')

# step 4
numbers = []
for _ in range(int(input())):
    numbers.append(int(input()))
del (numbers[numbers.index(max(numbers))])
del (numbers[numbers.index(min(numbers))])
print(*numbers, sep='\n')
numbers.remove()

# step 5
words = []
for _ in range(int(input())):
    words.append(input())

for ix, x in enumerate(words):
    for iy, y in enumerate(words):
        if x == y and ix != iy:
            del (words[iy])

print(*words, sep='\n')

# step 6
words = []
for _ in range(int(input())):
    words.append(input())
search = input()
for word in words:
    if word.lower().find(search.lower()) != -1:
        print(word)

# step 7
words = []
for _ in range(int(input())):
    words.append(input())

search = []
for _ in range(int(input())):
    search.append(input().lower())

for word in words:
    if all(x in word.lower() for x in search):
        print(word)
"""
# step 8
negatives = []
zeros = []
positives = []
for _ in range(int(input())):
    number = int(input())
    if number > 0:
        positives.append(number)
    elif number < 0:
        negatives.append(number)
    else:
        zeros.append(0)
print(*negatives, sep='\n')
print(*zeros, sep='\n')
print(*positives, sep='\n')
