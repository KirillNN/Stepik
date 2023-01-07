"""
# step 4
a = int(input())
b = int(input())

for i in range(a, b+1):
    print(chr(i), end=' ')

# step 5
s = input()
for c in s:
    print(ord(c), end=' ')
"""
# step 6
n = int(input())
s = input()
alpha = 'abcdefghijklmnopqrstuvwxyz'
for c in s:
    print(alpha[alpha.index(c) - n], end='')
