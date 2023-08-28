"""
#step 6
def matrix_multiply(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        raise ValueError(
            "Number of columns in the first matrix must be equal to the number of rows in the second matrix")

    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            sum = 0
            for k in range(len(matrix2)):
                sum += matrix1[i][k] * matrix2[k][j]
            row.append(sum)
        result.append(row)

    return result


matrix1 = [
    [1, 1, 1],
    [2, 2, 2],
    [3, 3, 3]
]

matrix2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = matrix_multiply(matrix1, matrix2)
for row in result:
    print(row)

#step 7
def matrix_multiply(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        raise ValueError(
            "Number of columns in the first matrix must be equal to the number of rows in the second matrix")

    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            sum = 0
            for k in range(len(matrix2)):
                sum += matrix1[i][k] * matrix2[k][j]
            row.append(sum)
        result.append(row)

    return result


matrix1 = [
    [1, -1, 0],
    [3, -4, 2]
]

matrix2 = [
    [1, 2],
    [3, 4],
    [5, 6]
]

result = matrix_multiply(matrix1, matrix2)
for row in result:
    print(row)

#step 8
def matrix_multiply(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        raise ValueError(
            "Number of columns in the first matrix must be equal to the number of rows in the second matrix")

    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            sum = 0
            for k in range(len(matrix2)):
                sum += matrix1[i][k] * matrix2[k][j]
            row.append(sum)
        result.append(row)

    return result


matrix1 = [
    [1, 0],
    [4, 1]
]

matrix2 = [
    [1, 0],
    [4, 1]
]

result = matrix_multiply(matrix1, matrix1)
result = matrix_multiply(result, matrix1)
for row in result:
    print(row)



# step 9 Напишите программу для вычисления суммы двух матриц
def input_matrix(n):
    matrix = []
    for _ in range(n):
        matrix.append([int(num) for num in input().split()])
    return matrix


def summ_matrix(m1, m2, n, m):
    for i in range(n):
        for j in range(m):
            m1[i][j] += m2[i][j]
    return m1


n, m = [int(num) for num in input().split()]
matrix_1 = input_matrix(n)
input()
matrix_2 = input_matrix(n)
matrix = summ_matrix(matrix_1, matrix_2, n, m)
for i in range(n):
    print(*matrix[i])

# step 10 Напишите программу, которая перемножает две матрицы.
def matrix_multiply(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        raise ValueError(
            "Number of columns in the first matrix must be equal to the number of rows in the second matrix")

    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            sum = 0
            for k in range(len(matrix2)):
                sum += matrix1[i][k] * matrix2[k][j]
            row.append(sum)
        result.append(row)

    return result


def input_matrix(n):  # передаем кол-во рядов
    matrix = []
    for _ in range(n):
        matrix.append([int(num) for num in input().split()])
    return matrix


n, m = [int(num) for num in input().split()]
matrix_1 = input_matrix(n)
input()
m, k = [int(num) for num in input().split()]
matrix_2 = input_matrix(m)
matrix = matrix_multiply(matrix_1, matrix_2)
for i in range(len(matrix)):
    print(*matrix[i])
"""


# step 11 Напишите программу, которая возводит квадратную матрицу в m-ую степень.
def matrix_multiply(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        raise ValueError(
            "Number of columns in the first matrix must be equal to the number of rows in the second matrix")

    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            sum = 0
            for k in range(len(matrix2)):
                sum += matrix1[i][k] * matrix2[k][j]
            row.append(sum)
        result.append(row)

    return result


def input_matrix(n):
    matrix = []
    for _ in range(n):
        matrix.append([int(num) for num in input().split()])
    return matrix


n = int(input())
matrix_base = input_matrix(n)
matrix = matrix_multiply(matrix_base, matrix_base)
m = int(input())
for i in range(m - 2):
    matrix = matrix_multiply(matrix, matrix_base)

for i in range(len(matrix)):
    print(*matrix[i])
