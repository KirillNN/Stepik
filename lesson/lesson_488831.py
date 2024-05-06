'''


'''
# step 1

data = {}
for _ in range(int(input())):
    key, value = input().split(': ')
    data[key.lower()] = value

query = []
for _ in range(int(input())):
    query.append(input().lower())

for i in query:
    print(data.get(i, 'Не найдено'))


