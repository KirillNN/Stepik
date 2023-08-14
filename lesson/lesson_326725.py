# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif',
#             'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
#             'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
#
# new_keywords = [x[1:] for x in keywords]
#
# print(new_keywords)
#
# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif',
#             'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
#             'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
#
# lengths = [len(x) for x in keywords]
#
# print(lengths)
#
# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif',
#             'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
#             'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
#
# new_keywords = [x for x in keywords if len(x) >= 5]
#
# print(new_keywords)
#
# palindromes = [x for x in range(100, 1000) if str(x) == str(x)[::-1]]
#
# print(palindromes)

# step 7
# n = int(input())
# result = [str(x ** 2) for x in range(1, n + 1)]
# print('\n'.join(result))

# step 8
# numbers = map(int, input().split())
# result = [x ** 3 for x in numbers]
# print(*result)

# step 9
# print('\n'.join(input().split()))

# step 10
# text = input()
# result = [x for x in text if x.isdigit()]
# print(*result, sep='')
#
# print(*[x for x in input() if x.isdigit()], sep='')

# step 11
numbers = map(int, input().split())
result = [x ** 2 for x in numbers if x ** 2 % 10 != 4 and not x % 2]
print(*result)
