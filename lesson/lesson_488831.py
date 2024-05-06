'''
# step 1

data = {}
for _ in range(int(input())):
    key, value = input().split(': ')
    data[key.lower()] = value

for _ in range(int(input())):
    print(data.get(input().lower(), 'Не найдено'))


# step 2
a = input()
b = input()

print(['NO', 'YES'][sorted(a) == sorted(b)])
'''
# step 3
a = [x for x in input().lower() if x.isalpha()]
b = [x for x in input().lower() if x.isalpha()]


print(['NO', 'YES'][sorted(a) == sorted(b)])