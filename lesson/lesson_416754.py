"""
# step 8
n = int(input())
m = int(input())
matrix = []
for i in range(n):
    matrix.append([input() for _ in range(m)])

for r in range(n):
    for c in range(m):
        print(matrix[r][c], end=' ')
    print()

# step 9
n = int(input())
m = int(input())
matrix = []
for i in range(n):
    matrix.append([input() for _ in range(m)])

for r in range(n):
    for c in range(m):
        print(matrix[r][c], end=' ')
    print()
print()
for r in range(m):
    for c in range(n):
        print(matrix[c][r], end=' ')
    print()

# step 10
n = int(input())
matrix = []  # матрица квадратная
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

result = 0
for i in range(n):
    result += matrix[i][i]

print(result)

# step 11
n = int(input())
# matrix = []  # матрица квадратная
result = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    x = sum(temp) / len(temp)
    result.append(sum([i > x for i in temp]))
print(*result, sep='\n')

# step 12
n = int(input())
matrix = []  # матрица квадратная
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

maximum = matrix[0][0]
for r in range(n):
    for c in range(r + 1):
        if matrix[r][c] > maximum:
            maximum = matrix[r][c]
print(maximum)

# step 13
n = int(input())
matrix = []  # матрица квадратная
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

maximum = matrix[0][0]
for i in range(n):
    for j in range(n):
        if any([j <= i <= n - 1 - j, j >= i >= n - 1 - j]) and matrix[i][j] > maximum:
            maximum = matrix[i][j]

print(maximum)
"""
# step 14
n = int(input())
matrix = []  # матрица квадратная
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

up, right, down, left = 0, 0, 0, 0

for i in range(n):
    for j in range(n):
        if i < j and i < n - 1 - j:  # up
            up += matrix[i][j]
        elif j > i > n - 1 - j:  # right
            right += matrix[i][j]
        elif i > j and i > n - 1 - j:  # down
            down += matrix[i][j]
        elif j < i < n - 1 - j:  # left
            left += matrix[i][j]

print(f'Верхняя четверть: {up}')
print(f'Правая четверть: {right}')
print(f'Нижняя четверть: {down}')
print(f'Левая четверть: {left}')
