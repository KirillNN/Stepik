"""
# step 1
n = int(input())
m = int(input())
matrix = []
for i in range(n):
    matrix.append([x * i for x in range(m)])

for r in range(n):
    for c in range(m):
        print(str(matrix[r][c]).ljust(3), end='')
    print()

# step 2
n = int(input())
m = int(input())
matrix = []
for i in range(n):
    matrix.append([int(num) for num in input().split()])

maximum, max_i, max_j = matrix[0][0], 0, 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] > maximum:
            maximum, max_i, max_j = matrix[i][j], i, j
print(max_i, max_j)

# step 3
n = int(input())
m = int(input())
matrix = []
for i in range(n):
    matrix.append([int(num) for num in input().split()])
x, y = [int(num) for num in input().split()]

for i in range(n):
    matrix[i][x], matrix[i][y] = matrix[i][y], matrix[i][x]

for i in range(n):
    print(*matrix[i])

# step 4
n = int(input())
matrix = []  # матрица квадратная
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

result = 'YES'
for i in range(n - 1):
    for j in range(i + 1, n):
        if matrix[i][j] != matrix[j][i]:
            result = 'NO'
            break

print(result)

# step 5
n = int(input())
matrix = []  # матрица квадратная
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

for i in range(n):
    matrix[i][i], matrix[n - i - 1][i] = matrix[n - i - 1][i], matrix[i][i]

for i in range(n):
    print(*matrix[i])

# step 6
n = int(input())
matrix = []  # матрица квадратная
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

for i in range(n // 2):
    matrix[i], matrix[n - 1 - i] = matrix[n - 1 - i], matrix[i]

for i in range(n):
    print(*matrix[i])
# step 7
n = int(input())
matrix = []  # матрица квадратная
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

rotated = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        rotated[j][n - i - 1] = matrix[i][j]

for i in range(n):
    print(*rotated[i])

# step 8
xy = input()
y = '87654321'.index(xy[1])
x = 'abcdefgh'.index(xy[0])
matrix = [['.'] * 8 for _ in range(8)]
matrix[y][x] = 'N'

for i in range(8):
    for j in range(8):
        if abs((x - j) * (y - i)) == 2:
            matrix[i][j] = '*'

for i in range(8):
    print(*matrix[i])
"""
# step 9
n = int(input())
matrix = []  # матрица квадратная
all_numbers = set()
result = 'YES'
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)
    all_numbers.update(temp)

# Суммы строк, столбцов и диагоналей
row_sums = [sum(row) for row in matrix]
col_sums = [sum(matrix[i][j] for i in range(n)) for j in range(n)]
main_diag_sum = sum(matrix[i][i] for i in range(n))
anti_diag_sum = sum(matrix[i][n - i - 1] for i in range(n))

# Сравнение всех сумм
total_sum = main_diag_sum  # Используем главную диагональ как эталонную сумму
all_sums = row_sums + col_sums + [main_diag_sum, anti_diag_sum]

# проверки
if not sum(row_sums) == sum(range(1, n ** 2 + 1)):
    result = 'NO'
if not all(s == total_sum for s in all_sums):
    result = 'NO'
if not len(all_numbers) == n ** 2:
    result = 'NO'

print(result)
