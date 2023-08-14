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
