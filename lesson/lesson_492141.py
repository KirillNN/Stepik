'''
# step 1
dnk = input()
data = dict(zip('GCTA', 'CGAU'))
result = ''
for i in dnk:
    result += data.get(i)
print(result)

# step 2
string = input().split()
data = {}
for word in string:
    if word in data:
        data[word] += 1
    else:
        data[word] = 1
    print(data.get(word), end=' ')

# step 3
d = {
    1: "AEILNORSTU",
    2: "DG",
    3: "BCMP",
    4: "FHVWY",
    5: "K",
    8: "JX",
    10: "QZ"
}
word = input()
count = 0
for letter in word:
    for i, v in d.items():
        if letter in v:
            count += i
            break
print(count)
# step 4
def build_query_string(params):
    data = []
    for i, v in params.items():
        data.append(f'{i}={v}')
    data.sort()
    return '&'.join(data)


print(build_query_string({'a': 'b', 'c': 'd', 'stepik': 'beegeek', 'iq': 'option', 'rita': 'ora'}))
# step 5
def merge(dict_list):
    merged_dict = {}
    for dictionary in dict_list:
        for key, value in dictionary.items():
            if key not in merged_dict:
                merged_dict[key] = set()
            merged_dict[key].add(value)
    return merged_dict

# step 6
data = {}
for _ in range(int(input())):
    k, *v = input().split()
    data[k] = v

for _ in range(int(input())):
    action, filename = input().split()
    if action == 'execute':
        action = 'X'
    elif action == 'write':
        action = 'W'
    else:
        action = 'R'

    for k, v in data.items():
        if k == filename:
            if action in v:
                print('OK')
            else:
                print('Access denied')
            break
'''
# step 7
data = {}
for _ in range(int(input())):
    customer, product, count = input().split()
    if customer in data:
        if product in data.get(customer):
            data[customer][product] += int(count)
        else:
            data[customer][product] = int(count)
    else:
        data[customer] = {product: int(count)}

for customer in sorted(data):
    print(f'{customer}:')
    for product in sorted(data[customer]):
        print(f'{product} {data[customer][product]}')
