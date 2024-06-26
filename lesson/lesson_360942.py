'''деление комплексных чисел'''
# a = 2
# b = 5
# c = 3
# d = 1
# first = (a * c + b * d) / (c * c + d * d)
# second = (b * c - a * d) / (c * c + d * d)
# if second > 0:
#     print(f'{first} + {second}i')
# elif second < 0:
#     print(f'{first} - {abs(second)}i')
# else:
#     print(first)

'''умножение комплексных чисел'''
# a = 1
# b = 1
# c = 1
# d = 1
# first = a * c - b * d
# second = a * d + b * c
# print(first, second)
'''
# step 12
z1 = complex(input())
z2 = complex(input())
print(f'{z1} + {z2} = {z1 + z2}')
print(f'{z1} - {z2} = {z1 - z2}')
print(f'{z1} * {z2} = {z1 * z2}')

# step 13
numbers = [3 + 4j, 3 + 1j, -7 + 3j, 4 + 8j, -8 + 10j, -3 + 2j, 3 - 2j, -9 + 9j, -1 - 1j, -1 - 10j, -20 + 15j, -21 + 1j, 1j, -3 + 8j, 4 - 6j, 8 + 2j, 2 + 3j]

print(max(numbers, key=abs))
print(abs(max(numbers, key=abs)))
'''
# step 14
n = int(input())
z1 = complex(input())
z2 = complex(input())
print(z1 ** n + z2 ** n + z1.conjugate() ** n + z2.conjugate() ** (n + 1))
