'''
# step 1
def concat(*args, sep=' '):
    return sep.join(map(str, args))


print(concat('hello', 'python', 'and', 'stepik'))
print(concat('hello', 'python', 'and', 'stepik', sep='*'))

# step 3
words = 'the world is mine take a look what you have started'.split()

print(*map(lambda x: f'"{x}"', words))

# step 4
numbers = [18, 191, 9009, 5665, 78, 77, 45, 23, 19991, 908, 8976, 6565, 5665, 10, 1000, 908, 909, 232, 45654, 786]

print(*filter(lambda x: str(x) != str(x)[::-1], numbers))

# step 5
numbers = [(10, -2, 3, 4), (-13, 56), (1, 9, 2), (-1, -9, -45, 32), (-1, 5, 1), (17, 0, 1), (0, 1), (3,), (39, 12),
           (11, -23), (10, -100, 21, 32), (3, -8), (1, 1)]

sorted_numbers = sorted(numbers, key=lambda x: -(sum(x) / len(x)))

print(sorted_numbers)

# step 6
def mul7(x):
    return x * 7


def add2(x, y):
    return x + y


def add3(x, y, z):
    return x + y + z

def call(func, *args):
    return func(*args)

print(call(mul7, 10))
print(call(add2, 2, 7))
print(call(add3, 10, 30, 40))
print(call(bool, 0))

# step 7
def add3(x):
    return x + 3


def mul7(x):
    return x * 7


def compose(f, g):
    def composed_function(x):
        return f(g(x))

    return composed_function


print(compose(mul7, add3)(1))
print(compose(add3, mul7)(2))
print(compose(mul7, str)(3))
print(compose(str, mul7)(5))


# step 8
import operator

def arithmetic_operation(op):
    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }
    return operations[op]

# Примеры использования:

add = arithmetic_operation('+')
div = arithmetic_operation('/')

print(add(10, 20))  # Результат должен быть 30
print(div(20, 5))   # Результат должен быть 4.0


# step 9
def sort_words_ignore_case(input_string):
    # Разделяем строку на слова
    words = input_string.split()
    # Сортируем слова независимо от регистра
    sorted_words = sorted(words, key=str.lower)
    # Объединяем отсортированные слова в строку и выводим
    result = ' '.join(sorted_words)
    return result

# Пример использования:
input_string = input()
sorted_string = sort_words_ignore_case(input_string)
print(sorted_string)

# step 10
def gematria(word):
    # Преобразуем слово в верхний регистр
    word_upper = word.upper()
    # Вычисляем сумму числовых значений букв
    return sum(ord(char) - ord('A') for char in word_upper)


# Считываем количество слов
n = int(input())
words = [input().strip() for _ in range(n)]

# Сортируем слова по гематрии, затем лексикографически
sorted_words = sorted(words, key=lambda word: (gematria(word), word))

# Выводим отсортированные слова
for word in sorted_words:
    print(word)
'''


# step 11
def ip_to_decimal(ip):
    # Разделяем IP-адрес на октеты и преобразуем их в целые числа
    octets = list(map(int, ip.split('.')))
    # Преобразуем IP-адрес в десятичное число
    decimal_value = (octets[0] << 24) + (octets[1] << 16) + (octets[2] << 8) + octets[3]
    return decimal_value


# Считываем количество IP-адресов
n = int(input())
# Считываем сами IP-адреса
ip_addresses = [input().strip() for _ in range(n)]

# Сортируем IP-адреса по их десятичному представлению
sorted_ips = sorted(ip_addresses, key=ip_to_decimal)

# Выводим отсортированные IP-адреса
for ip in sorted_ips:
    print(ip)
