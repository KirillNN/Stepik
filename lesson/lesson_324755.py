# step 7

# ip = map(int, input().split('.'))
#
# for item in ip:
#     if item <0 or item > 255:
#         print('НЕТ')
#         break
# else:
#     print('ДА')


# step 8
# string = input()
# delimiter = input()
# print(delimiter.join(string))

# step 9
numbers = tuple(map(int, input().split()))
result = 0
for i, v_i in enumerate(numbers):
    for j, v_j in enumerate(numbers):
        if i != j and v_i == v_j:
            result += 1

print(int(result / 2))
