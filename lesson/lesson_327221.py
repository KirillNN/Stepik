# step 1
# n = int(input())
# result = [x for x in range(2, n + 1, 2)]
# print(result)

# step 2
# L = map(int, input().split())
# M = map(int, input().split())

# result = [x + y for x, y in zip(L, M)]
# print(*result)

# step 3
# numbers = list(map(int, input().split()))
# print(*numbers, sep='+', end='=')
# print(sum(numbers))

# step 3
phone = input().split('-')
flag = True
if len(phone) == 4:
    for i, v in enumerate(phone):
        if i == 0 and v != '7':
            flag = False
        elif i in [1, 2] and (len(v) != 3 or not v.isdigit()):
            flag = False
        elif i == 3 and (len(v) != 4 or not v.isdigit()):
            flag = False
elif len(phone) == 3:
    for i, v in enumerate(phone):
        if i in [0, 1] and (len(v) != 3 or not v.isdigit()):
            flag = False
        elif i == 2 and (len(v) != 4 or not v.isdigit()):
            flag = False
else:
    flag = False

print('YES' if flag else 'NO')

# 2 вариант
seq = input().split("-")
lens = [len(el) for el in seq]

if lens == [1, 3, 3, 4] and "".join(seq).isdigit() and seq[0] == "7":
    print("YES")
elif lens == [3, 3, 4] and "".join(seq).isdigit():
    print("YES")
else:
    print("NO")

# step 5
print(max([len(el) for el in input().split()]))

# step 6
text = input()
words = text.split()

transformed_words = [word[1:] + word[0] + "ки" for word in words]
result = ' '.join(transformed_words)

print(result)
