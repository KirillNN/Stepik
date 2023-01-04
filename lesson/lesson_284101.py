# step 7
# word = input()
# for index, value in enumerate(word):
#     if index % 2 == 0:
#         print(value)

# step 8
# word = input()
# for i in word[::-1]:
#     print(i)

# step 9
# a, b, c = input(), input(), input()
# print(b[0] + a[0] + c[0])

# step 10
# number = int(input())
# summ = 0
# while number > 0:
#     summ += number % 10
#     number //= 10
# print(summ)

# step 11
# print('Цифра') if any([x.isdigit() for x in input()]) else print('Цифр нет')

# step 12
# word = input()
# print(f'Символ + встречается {word.count("+")} раз')
# print(f'Символ * встречается {word.count("*")} раз')

# step 13
# word = input()
# count = 0
# for i, j in zip(word, word[1:]):
#     if i == j:
#         count += 1
# print(count)

# step 14
# sentence = input().lower()
# vowel = ('а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е')
# consonant = ('б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ')
# count_vowel = sum(map(lambda x: x in vowel, sentence))
# count_consonant = sum(map(lambda x: x in consonant, sentence))
# print(f'Количество гласных букв равно {count_vowel}')
# print(f'Количество согласных букв равно {count_consonant}')

# step 15
number = int(input())
print(f'{number:b}')
