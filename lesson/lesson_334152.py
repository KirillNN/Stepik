# step 4
# объявление функции
def draw_triangle():
    n = 8
    for i in range(n):
        print(' ' * (n - 1) + '*' * (i * 2 + 1))
        n -= 1


# основная программа
draw_triangle()  # вызов функции


# step 5
# объявление функции
def get_shipping_cost(quantity):
    return 1000 + (quantity - 1) * 120


# считываем данные
n = int(input())

# вызываем функцию
print(get_shipping_cost(n))

# step 6
from math import factorial


# объявление функции
def compute_binom(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))


# считываем данные
n = int(input())
k = int(input())

# вызываем функцию
print(compute_binom(n, k))


# step 7
# объявление функции
def number_to_words(num):
    return \
        ['ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять', 'одиннадцать',
         'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать',
         'девятнадцать', 'двадцать', 'двадцать один', 'двадцать два', 'двадцать три', 'двадцать четыре',
         'двадцать пять',
         'двадцать шесть', 'двадцать семь', 'двадцать восемь', 'двадцать девять', 'тридцать', 'тридцать один',
         'тридцать два', 'тридцать три', 'тридцать четыре', 'тридцать пять', 'тридцать шесть', 'тридцать семь',
         'тридцать восемь', 'тридцать девять', 'сорок', 'сорок один', 'сорок два', 'сорок три', 'сорок четыре',
         'сорок пять', 'сорок шесть', 'сорок семь', 'сорок восемь', 'сорок девять', 'пятьдесят', 'пятьдесят один',
         'пятьдесят два', 'пятьдесят три', 'пятьдесят четыре', 'пятьдесят пять', 'пятьдесят шесть', 'пятьдесят семь',
         'пятьдесят восемь', 'пятьдесят девять', 'шестьдесят', 'шестьдесят один', 'шестьдесят два', 'шестьдесят три',
         'шестьдесят четыре', 'шестьдесят пять', 'шестьдесят шесть', 'шестьдесят семь', 'шестьдесят восемь',
         'шестьдесят девять', 'семьдесят', 'семьдесят один', 'семьдесят два', 'семьдесят три', 'семьдесят четыре',
         'семьдесят пять', 'семьдесят шесть', 'семьдесят семь', 'семьдесят восемь', 'семьдесят девять', 'восемьдесят',
         'восемьдесят один', 'восемьдесят два', 'восемьдесят три', 'восемьдесят четыре', 'восемьдесят пять',
         'восемьдесят шесть', 'восемьдесят семь', 'восемьдесят восемь', 'восемьдесят девять', 'девяносто',
         'девяносто один',
         'девяносто два', 'девяносто три', 'девяносто четыре', 'девяносто пять', 'девяносто шесть', 'девяносто семь',
         'девяносто восемь', 'девяносто девять'][num]


# считываем данные
n = int(input())

# вызываем функцию
print(number_to_words(n))


# step 8
# объявление функции
def get_month(language, number):
    mounth_ru = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь',
                 'Ноябрь', 'Декабрь']
    mounth_en = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                 'November', 'December']
    if language == 'ru':
        return mounth_ru[number - 1].lower()
    return mounth_en[number - 1].lower()


# считываем данные
lan = input()
num = int(input())

# вызываем функцию
print(get_month(lan, num))


# step 9
# объявление функции
def is_magic(date):
    day, month, year = map(int, date.split('.'))
    if day * month == year % 100:
        return True
    return False


# считываем данные
date = input()

# вызываем функцию
print(is_magic(date))


# step 10
# объявление функции
def is_pangram(text):
    return len(set([x.lower() for x in text if x.isalpha()])) == 26


# считываем данные
text = input()

# вызываем функцию
print(is_pangram(text))
