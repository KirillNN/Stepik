# step 8
# объявление функции
def draw_triangle(fill, base):
    t_side = [fill * x for x in range(1, (base + 1) // 2)]
    t_middle = [fill * ((base + 1) // 2)]
    triangle = t_side + t_middle + t_side[::-1]
    print(*triangle, sep='\n')


# считываем данные
fill = input()
base = int(input())

# вызываем функцию
draw_triangle(fill, base)


# step 9
# объявление функции
def print_fio(name, surname, patronymic):
    print((surname[0] + name[0] + patronymic[0]).upper())


# считываем данные
name, surname, patronymic = input(), input(), input()

# вызываем функцию
print_fio(name, surname, patronymic)


# step 10
# объявление функции
def print_digit_sum(num):
    result = 0
    while num > 0:
        result += num % 10
        num //= 10
    print(result)


# считываем данные
n = int(input())

# вызываем функцию
print_digit_sum(n)
