"""
n, m = int(input()), int(input())

my_list = [[0] * m ] * n
print(my_list)
my_list[0][0] = 17

print(my_list)

# step 8
n = int(input())
list = []
for _ in range(n):
    list.append([x for x in range(1, n + 1)])

print(*list, sep='\n')

# step 9
n = int(input())
list = []
for i in range(n):
    list.append([x for x in range(1, i + 2)])
print(*list, sep='\n')

# step 10
def pascal(n):
    list = [[1], [1, 1]]
    for i in range(n - 1):
        list.append([1, *[a + b for a, b in zip(list[i + 1], list[i + 1][1:])], 1])
    return list[n]


n = int(input())
print(pascal(n))
"""


# step 11
def pascal(n):
    list = [[1]]
    for i in range(n - 1):
        list.append([1, *[a + b for a, b in zip(list[i], list[i][1:])], 1])
    return list


n = int(input())
for row in pascal(n):
    print(*row)
