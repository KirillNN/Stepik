"""
# step 7
s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[:12])

# step 8
s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[-9:])

# step 9
s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[::7])

# step 10
s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[::-1])

# step 11
word = input()
print('YES') if word == word[::-1] else print('NO')

# step 12
word = input()
print(len(word))
print(word * 3)
print(word[0])
print(word[:3])
print(word[-3:])
print(word[::-1])
print(word[1:-1])

# step 13
word = input()
print(word[2])
print(word[-2])
print(word[:5])
print(word[:-2])
print(word[::2])
print(word[1::2])
print(word[::-1])
print(word[::-2])
"""
# step 14
word = input()
part_1 = ''
part_2 = ''
for index, value in enumerate(word):
    if index >= len(word) / 2:
        part_2 += value
    else:
        part_1 += value
print(part_2 + part_1)
