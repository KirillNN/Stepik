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
"""
#step 9
n, m = [int(num) for num in input().split()]
