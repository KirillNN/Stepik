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
"""
# step 2
