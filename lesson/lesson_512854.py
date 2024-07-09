'''
# step 5
func = lambda x: not x % 19 or not x % 13

# step 6
func = lambda x: x.lower()[0] == x.lower()[-1] == 'a'

# step 7
is_non_negative_num = lambda x: x.count('.') < 2 and not x.startswith('-') and x.lower() == x.upper()
print(is_non_negative_num('10.45'))

# step 8
is_num = lambda x: x.find('-') < 1 and x.count('-') < 2 and x.count('.') < 2 and x.lower() == x.upper()

# step 9
words = ['beverage', 'monday', 'abroad', 'bias', 'abuse', 'abolish', 'abuse', 'abuse', 'bid', 'wednesday', 'able',
         'betray', 'accident', 'abduct', 'bigot', 'bet', 'abandon', 'besides', 'access', 'friday', 'bestow', 'abound',
         'absent', 'beware', 'abundant', 'abnormal', 'aboard', 'about', 'accelerate', 'abort', 'thursday', 'tuesday',
         'sunday', 'berth', 'beyond', 'benevolent', 'abate', 'abide', 'bicycle', 'beside', 'accept', 'berry',
         'bewilder', 'abrupt', 'saturday', 'accessory', 'absorb']

result = filter(lambda x: len(x) == 6, words)
print(*sorted(result))

# step 10
numbers = [46, 61, 34, 17, 56, 26, 93, 1, 3, 82, 71, 37, 80, 27, 77, 94, 34, 100, 36, 81, 33, 81, 66, 83, 41, 80, 80,
           93, 40, 34, 32, 16, 5, 16, 40, 93, 36, 65, 8, 19, 8, 75, 66, 21, 72, 32, 41, 59, 35, 64, 49, 78, 83, 27, 57,
           53, 43, 35, 48, 17, 19, 40, 90, 57, 77, 56, 80, 95, 90, 27, 26, 6, 4, 23, 52, 39, 63, 74, 15, 66, 29, 88, 94,
           37, 44, 2, 38, 36, 32, 49, 5, 33, 60, 94, 89, 8, 36, 94, 46, 33]

result = filter(lambda x: not (x % 2 and x > 47), numbers)
result = map(lambda x: x // 2 if not x % 2 else x, result)
print(*result)

# step 11
from functools import reduce

data = [(19542209, 'New York'), (4887871, 'Alabama'), (1420491, 'Hawaii'), (626299, 'Vermont'),
        (1805832, 'West Virginia'), (39865590, 'California'), (11799448, 'Ohio'), (10711908, 'Georgia'),
        (10077331, 'Michigan'), (10439388, 'Virginia'), (7705281, 'Washington'), (7151502, 'Arizona'),
        (7029917, 'Massachusetts'), (6910840, 'Tennessee')]

data = sorted(data, key=lambda x: x[1][-1], reverse=True)
print(*[f'{y}: {x}' for x, y in data], sep='\n')

# step 12
data = ['год', 'человек', 'время', 'дело', 'жизнь', 'день', 'рука', 'раз', 'работа', 'слово', 'место', 'лицо', 'друг',
        'глаз', 'вопрос', 'дом', 'сторона', 'страна', 'мир', 'случай', 'голова', 'ребенок', 'сила', 'конец', 'вид',
        'система', 'часть', 'город', 'отношение', 'женщина', 'деньги']

print(*sorted(data, key=lambda x: (len(x), x)))

# step 13
mixed_list = ['tuesday', 'abroad', 'abuse', 'beside', 'monday', 'abate', 'accessory', 'absorb', 1384878, 'sunday',
              'about', 454805, 'saturday', 'abort', 2121919, 2552839, 977970, 1772933, 1564063, 'abduct', 901271,
              2680434, 'bicycle', 'accelerate', 1109147, 942908, 'berry', 433507, 'bias', 'bestow', 1875665, 'besides',
              'bewilder', 1586517, 375290, 1503450, 2713047, 'abnormal', 2286106, 242192, 701049, 2866491, 'benevolent',
              'bigot', 'abuse', 'abrupt', 343772, 'able', 2135748, 690280, 686008, 'beyond', 2415643, 'aboard', 'bet',
              859105, 'accident', 2223166, 894187, 146564, 1251748, 2851543, 1619426, 2263113, 1618068, 'berth',
              'abolish', 'beware', 2618492, 1555062, 'access', 'absent', 'abundant', 2950603, 'betray', 'beverage',
              'abide', 'abandon', 2284251, 'wednesday', 2709698, 'thursday', 810387, 'friday', 2576799, 2213552,
              1599022, 'accept', 'abuse', 'abound', 1352953, 'bid', 1805326, 1499197, 2241159, 605320, 2347441]

print(max(mixed_list, key=lambda x: x if isinstance(x, int) else 0))

# step 14
mixed_list = ['a', 'ab', 3, 5, 1, 8, 0, 'c', 'ac', 'aab']
print(*sorted(mixed_list, key=str))

# step 15
print(*map(lambda x: 255 - x, map(int, input().split())))
'''

# step 16
from functools import reduce

evaluate = lambda coefficients, x: reduce(lambda a, b: a * x + b, coefficients)

coefficients = map(int, input().split())
x = int(input())

print(evaluate(coefficients, x))
