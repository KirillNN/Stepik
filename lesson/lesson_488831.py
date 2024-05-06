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

# step 3
a = [x for x in input().lower() if x.isalpha()]
b = [x for x in input().lower() if x.isalpha()]

print(['NO', 'YES'][sorted(a) == sorted(b)])

# step 4
data = {}
for _ in range(int(input())):
    k, v = input().split()
    data[k] = v

word = input()
for k, v in data.items():
    if word == k:
        print(v)
        break
    elif word == v:
        print(k)
        break
'''
# step 5
data = {}
for _ in range(int(input())):
    k, *v = input().split()
    data[k] = v

for _ in range(int(input())):
    city = input()
    for k, v in data.items():
        if city in v:
            print(k)
            break
