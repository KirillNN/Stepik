# step 5
# numbers = [8, 9, 10, 11]
# numbers[1] = 17
# numbers.append(4)
# numbers.append(5)
# numbers.append(6)
# numbers.pop(0)
# numbers += numbers
# numbers.insert(3, 25)
# print(numbers)

# step 6
# numbers = list(map(int, input().split()))
# min_number = numbers.index(min(numbers))
# max_number = numbers.index(max(numbers))
#
# numbers[max_number], numbers[min_number] = numbers[min_number], numbers[max_number]
# print(*numbers)

# step 7
# text = input().lower().split()
#
# result = text.count('a') + text.count('an') + text.count('the')
#
# print(f'Общее количество артиклей: {result}')

# step 8
# n = int(input()[1:])
# text = []
# for _ in range(n):
#     line = input()
#     x = line.find('#')
#     if x != -1:
#         text.append(line[:x].rstrip())
#     else:
#         text.append(line)
#
# print('\n'.join(text))

# step 10
# numbers = [4, 2, 8, 6, 5, 3, 10, 4, 100, 1, -7]
# numbers.sort()
# del numbers[0]
# del numbers[-1]
# numbers.sort(reverse=True)
# print(numbers)

# step 11
numbers = list(map(int, input().split()))
numbers.sort()
print(*numbers)
numbers.sort(reverse=True)
print(*numbers)
