"""
# step 1
n, m = [int(num) for num in input().split()]
matrix = [['.'] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if (not i % 2 and j % 2) or (i % 2 and not j % 2):
            matrix[i][j] = '*'

for i in range(n):
    print(*matrix[i])

# step 2
n = int(input())
matrix = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n - i - 1, n):
        if j == n - i - 1:  # условие для побочной диагонали
            matrix[i][j] = 1
        else: # сюда попадают все индексы правее побочной диагонали
            matrix[i][j] = 2

for i in range(n):
    print(*matrix[i])

# step 3
n, m = [int(num) for num in input().split()]

matrix = []
for i in range(n):
    matrix.append([m * i + (x + 1) for x in range(m)])

for r in range(n):
    for c in range(m):
        print(str(matrix[r][c]).ljust(3), end='')
    print()

# step 4
n, m = [int(num) for num in input().split()]

matrix = []
for i in range(n):
    matrix.append([i + x for x in range(1, n * (m - 1) + 2, n)])

for r in range(n):
    for c in range(m):
        print(str(matrix[r][c]).ljust(3), end='')
    print()

# step 5
n = int(input())
matrix = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if j == n - i - 1:  # условие для побочной диагонали
            matrix[i][j] = 1
        elif i == j:  # условие для главной диагонали
            matrix[i][j] = 1

for r in range(n):
    for c in range(n):
        print(str(matrix[r][c]).ljust(3), end='')
    print()

# step 6
n = int(input())
matrix = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i <= j and i <= n - 1 - j:  # верх + главная
            matrix[i][j] = 1
        elif i >= j and i >= n - 1 - j:  # низ + побочная
            matrix[i][j] = 1

for r in range(n):
    for c in range(n):
        print(str(matrix[r][c]).ljust(3), end='')
    print()

# step 7
n, m = [int(num) for num in input().split()]

matrix = []
for shift in range(n): # сдвиг влево на shift позиций
    original_list = list(range(1, m + 1))
    for _ in range(shift):
        temp_lst = original_list[0]
        for i in range(1, len(original_list)):
            original_list[i - 1] = original_list[i]
        original_list[-1] = temp_lst
    matrix.append(original_list)

for r in range(n):
    for c in range(m):
        print(str(matrix[r][c]).ljust(3), end='')
    print()
"""
# step 8
n, m = [int(num) for num in input().split()]

matrix = []
for i in range(n):
    temp = list(range(m * i + 1, m * (i + 1) + 1))
    if not i % 2:
        matrix.append(temp)
    else:
        temp.reverse()
        matrix.append(temp)

for r in range(n):
    for c in range(m):
        print(str(matrix[r][c]).ljust(3), end='')
    print()
