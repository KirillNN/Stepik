# step 6
# # объявление функции
# def convert_to_miles(km):
#     return km * 0.6214
#
#
# # считываем данные
# num = int(input())
#
# # вызываем функцию
# print(convert_to_miles(num))

# step 7
# объявление функции
# def get_days(month):
#     return {month in (1, 3, 5, 7, 8, 10, 12): 31,
#             month in (4, 6, 9, 11): 30,
#             month == 2: 28}[True]
#
#
# # считываем данные
# num = int(input())
#
# # вызываем функцию
# print(get_days(num))
#
#
# # step 8
# # объявление функции
# def get_factors(num):
#     result = []
#     for i in range(1, num + 1):
#         if not num % i:
#             result.append(i)
#     return result
#
#
# # считываем данные
# n = int(input())
#
# # вызываем функцию
# print(get_factors(n))
#
#
# # step 9
# # объявление функции
# def number_of_factors(num):
#     result = 0
#     for i in range(1, num // 2 + 1):
#         if not num % i:
#             result += 1
#     return result + 1
#
#
# # считываем данные
# n = int(input())
#
# # вызываем функцию
# print(number_of_factors(n))
#
#
# # step 10
# # объявление функции
# def find_all(target, symbol):
#     result = []
#     for index, letter in enumerate(target):
#         if letter == symbol:
#             result.append(index)
#     return result
#
#
# # считываем данные
# s = input()
# char = input()
#
# # вызываем функцию
# print(find_all(s, char))
#
#
# # step 11
# # объявление функции
# def merge(list1, list2):
#     return sorted(list1 + list2)
#
#
# # считываем данные
# numbers1 = [int(c) for c in input().split()]
# numbers2 = [int(c) for c in input().split()]
#
# # вызываем функцию
# print(merge(numbers1, numbers2))


# step 13
def quick_merge(args):
    result = []
    for i in args:
        result.extend(i)
    return sorted(result)


n = int(input())
lists = [list(map(int, input().split())) for _ in range(n)]
print(*quick_merge(lists))
