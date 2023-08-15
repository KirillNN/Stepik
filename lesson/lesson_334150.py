# step 2
# объявление функции
def is_valid_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    return False


# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
print(is_valid_triangle(a, b, c))


# step 3
# объявление функции
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if not num % i:
            return False
    return True


# считываем данные
n = int(input())

# вызываем функцию
print(is_prime(n))

# step 4
# Напишите функцию get_next_prime(num), которая принимает в качестве аргумента натуральное число num
# и возвращает первое простое число большее числа num.
# объявление функции

def get_next_prime(num):
    while True: # TODO: доделать
        for i in range(num, int(num ** 0.5) + 1):
            if not num % i:
                return False
        return True

# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))