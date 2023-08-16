# step 2
# объявление функции
def is_valid_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    return False


# # считываем данные
# a, b, c = int(input()), int(input()), int(input())
#
# # вызываем функцию
# print(is_valid_triangle(a, b, c))


# step 3
# объявление функции
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if not num % i:
            return False
    return True


# # считываем данные
# n = int(input())
#
# # вызываем функцию
# print(is_prime(n))


# step 4
# Напишите функцию get_next_prime(num), которая принимает в качестве аргумента натуральное число num
# и возвращает первое простое число большее числа num.
# объявление функции

def get_next_prime(num):
    while True:
        num += 1
        for i in range(2, int(num ** 0.5) + 1):
            if not num % i:
                break
        else:
            return num


# считываем данные
# n = int(input())
#
# # вызываем функцию
# print(get_next_prime(n))


# step 5
# Напишите функцию is_password_good(password), которая принимает
# в качестве аргумента строковое значение пароля password
# и возвращает значение True, если пароль является надежным
# и False - в противном случае.
# объявление функции
def is_password_good(password):
    flag = True
    if len(password) < 8:
        flag = False
    elif not any([x.isupper() for x in password]):
        flag = False
    elif not any([x.islower() for x in password]):
        flag = False
    elif not any([x.isdigit() for x in password]):
        flag = False
    return flag


# считываем данные
# txt = input()

# вызываем функцию
# print(is_password_good(txt))


# step 6
# Напишите функцию is_one_away(word1, word2), которая принимает
# в качестве аргументов два слова word1 и word2 и возвращает
# значение True, если слова имеют одинаковую длину и
# отличаются ровно в 1 символе и False - в противном случае.
# объявление функции
def is_one_away(word1, word2):
    if len(word1) != len(word2):
        return False
    elif [x == y for x, y in zip(word1, word2)].count(False) != 1:
        return False
    return True


# считываем данные
# txt1 = 'bike'
# txt2 = 'hike'
#
# # вызываем функцию
# print(is_one_away(txt1, txt2))


# step 7
# Напишите функцию is_palindrome(text), которая принимает в качестве
# аргумента строку text и возвращает значение True если
# указанный текст является палиндромом и False в противном случае.

# объявление функции
def is_palindrome(text):
    text = [x.lower() for x in text if x.isalpha()]
    return text == text[::-1]


# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))
