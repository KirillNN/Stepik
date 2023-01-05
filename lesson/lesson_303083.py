"""
# step 8
sentence = input().split()
print(len(sentence))

# step 9
word = input().lower()
print(f'Аденин: {word.count("а")}')
print(f'Гуанин: {word.count("г")}')
print(f'Цитозин: {word.count("ц")}')
print(f'Тимин: {word.count("т")}')

# step 10
n = int(input())
count = 0
for _ in range(n):
    word = input()
    if word.count('11') > 2:
        count += 1
print(count)

# step 11
word = input()
count = 0
for i in word:
    if i.isdigit():
        count += 1
print(count)

# step 12
word = input()
if word.endswith('.com') or word.endswith('.ru'):
    print('YES')
else:
    print('NO')

# step 13
s = input()
max_count = 0
max_char = ''
for c in s:
    if s.count(c) >= max_count:
        max_count = s.count(c)
        max_char = c
print(max_char)

# step 14
s = input()
if not s.count('f'):
    print('NO')
elif s.count('f') == 1:
    print(s.index('f'))
else:
    print(f"{s.index('f')} {s.rindex('f')}")
"""
# step 15
s = input()
first = s.index('h')
last = s.rindex('h')
result = s[:first] + s[last + 1:]
print(result)
