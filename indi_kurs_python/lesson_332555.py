# step 2
# http://codeforces.com/problemset/problem/268/A

# step 3
# rows, cols = map(int, input().split())
# m = [['.'] * (cols + 2)]  # расширяем матрицу
# for i in range(rows):
#     row = list(input())
#     m.append(['.'] + row + ['.'])
# m.append(['.'] * (cols + 2))
# print(*m)
# print()
# count = 0
# for i in range(1, rows + 1):
#     for j in range(1, cols + 1):
#         x = {m[i - 1][j], m[i + 1][j], m[i][j - 1], m[i][j + 1]}
#         if x == {'.'} and m[i][j] == '.':
#             count += 1
# print(count)

# step 4
# rows, cols = map(int, input().split())
# for row in range(rows):
#     print(*range(row * cols, (row + 1) * cols)[::(-1) ** row])

# step 5
# rows, cols = map(int, input().split())
# result = '#Black&White'
#
# for _ in range(rows):
#     if set(input().split()) & set('CMY'):
#         result = '#Color'
#         break
#
# print(result)

# step 6
n = int(input())
m = [[1] * (n + 2)]  # расширяем матрицу
for i in range(n):
    m.append([1] + [0] * n + [1])
m.append([[1] * (n + 2)])  # расширяем матрицу
print(m)
direction = ['right', 'down', 'left', 'up']
count = 1
i = j = 0
while count < n:
    pass
