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
"""
# step 9