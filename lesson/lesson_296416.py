"""
s = 'i Learn Python language'
print(s.capitalize())

s = 'i LEARN Python LAnguaGE'
print(s.lower())

s = 'i LEARN Python LAnguaGE'
print(s.upper())

s = 'i LEARN Python LAnguaGE'
print(s.swapcase())

# step 8
name, surname = input().split()
if name == name.title() and surname == surname.title():
    print('YES')
else:
    print('NO')

# step 9
print(input().swapcase())

# step 10
sentence = input().lower()
if sentence.find('хорош') == -1:
    print('NO')
else:
    print('YES')
"""
# step 11
sentence = input()
count = 0
for i in sentence:
    if i.islower():
        count += 1
print(count)
