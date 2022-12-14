# step 6
# n = int(input())
#
# max_digit = -1
# while n > 0:
#     digit = n % 10
#     if digit % 3 == 0:
#         if digit > max_digit:
#             max_digit = digit
#     n //= 10
# if max_digit < 0:
#     print('NO')
# else:
#     print(max_digit)

# step 7
# n = int(input())
# res = -1
# while n > 0:
#     res = n
#     n //= 10
# print(res)

# step 8
n = int(input())
product = 1
while n > 0:
    digit = n % 10
    product *= digit
    n //= 10
print(product)
