"""
s = 'Python rocks!'
print(s.replace('o', '@'))

# step 7
s = input()
result = ''
for i, c in enumerate(s):
    if i % 3 != 0:
        result += c
print(result)

# step 8
s = input()
print(s.replace('1', 'one'))

# step 9
s = input()
print(s.replace('@', ''))

# step 10
s = input()
if s.count('f') == 0:
    print(-2)
elif s.count('f') == 1:
    print(-1)
else:
    i = s.index('f')
    print(s.index('f', i + 1))
"""
# step 11
s = input()
first = s.find('h')
last = s.rfind('h')
tmp = s[last - 1:first:-1]
print(s[:first + 1] + tmp + s[last:])
