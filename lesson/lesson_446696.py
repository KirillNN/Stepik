'''
# step 10
result = {i: i ** 2 for i in range(1, 16)}
print(result)

# step 11
dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98,
         't': 76, 'q': 34, 'f': 90, 'm': 230}
dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123,
         'w': 111, 'z': 666}

result = dict1.copy()
for key, value in dict2.items():
    if key in result:
        result[key] += dict2[key]
    else:
        result[key] = dict2[key]

print(result)

# step 12
text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'

result = {x: text.count(x) for x in text}

print(result)

# step 13
s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'.split()

dict1 = {x: s.count(x) for x in s}
print(sorted([i for i, v in dict1.items() if v == max(dict1.values())])[0])

# step 14
pets = [('Hatiko', 'Parker', 'Wilson', 50),
        ('Rusty', 'Josh', 'King', 25),
        ('Fido', 'John', 'Smith', 28),
        ('Butch', 'Jake', 'Smirnoff', 18),
        ('Odi', 'Emma', 'Wright', 18),
        ('Balto', 'Josh', 'King', 25),
        ('Barry', 'Josh', 'King', 25),
        ('Snape', 'Hannah', 'Taylor', 40),
        ('Horry', 'Martha', 'Robinson', 73),
        ('Giro', 'Alex', 'Martinez', 65),
        ('Zooma', 'Simon', 'Nevel', 32),
        ('Lassie', 'Josh', 'King', 25),
        ('Chase', 'Martha', 'Robinson', 73),
        ('Ace', 'Martha', 'Williams', 38),
        ('Rocky', 'Simon', 'Nevel', 32)]

result = {}
for dog, name, surname, age in pets:
    if (name, surname, age) in result:
        result[name, surname, age] += [dog]
    else:
        result[name, surname, age] = [dog]

print(result)
# step 15
import re
text = re.sub(r"[.,!?:;-]", "", input().lower()).split()
dict1 = {x: text.count(x) for x in text}
print(sorted([i for i, v in dict1.items() if v == min(dict1.values())])[0])
'''
# step 16
text = input().split()

result = []
counter = {}
for i in text:
    if i in counter:
        counter[i] += 1
        result.append(f'{i}_{counter[i]}')
    else:
        counter[i] = 0
        result.append(i)

print(' '.join(result))


