'''
# step 1

data = {}
for _ in range(int(input())):
    key, value = input().split(': ')
    data[key.lower()] = value

for _ in range(int(input())):
    print(data.get(input().lower(), 'Не найдено'))

'''
# step 2
