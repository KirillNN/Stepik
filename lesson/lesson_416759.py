"""
# step 1
text = input().split()
n = int(input())
matrix = []
for i in range(n):
    matrix.append(text[i::n])
print(matrix)

# step 2
n = int(input())
matrix = []  # матрица квадратная
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

maximum = matrix[0][0]
for i in range(n):
    for j in range(n):
        if j >= i >= n - 1 - j and matrix[i][j] > maximum:  # right + побочная
            maximum = matrix[i][j]
        elif i > j and i >= n - 1 - j and matrix[i][j] > maximum:  # down + побочная
            maximum = matrix[i][j]

print(maximum)

# step 3
n = int(input())
matrix = []  # матрица квадратная
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

for i in range(n):
    for j in range(n):
        print(matrix[j][i], end=' ')
    print()
"""
# step 4
n = int(input())
matrix = [['.'] * n for _ in range(n)]  # матрица квадратная
for i in range(n):
    for j in range(n):
        if i == n // 2 or j == n // 2:
            matrix[i][j] = '*'
        elif j == n - i - 1:  # условие для побочной диагонали
            matrix[i][j] = '*'
        elif i == j:  # условие для главной диагонали
            matrix[i][j] = '*'

for i in range(len(matrix)):
    print(*matrix[i])
