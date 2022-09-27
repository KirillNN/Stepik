# n = int(input())
# summ = 0
# for i in range(n):
#     summ += list(map(int, input().split()))[i]
# print(summ)


# n = int(input())
# matrix = []
# for i in range(n):
#     matrix.append(input().split())
# for i in range(n):
#     for j in range(n):
#         print(matrix[j][i], end=' ')
#     print()

# n = int(input())
# matrix = []
# for i in range(n):
#     matrix.append(input().split())
# for i in range(n - 1, -1, -1):
#     for j in range(n - 1, -1, -1):
#         print(matrix[j][i], end=' ')
#     print()

# rows, cols = map(int, input().split())
# matrix = []
# for i in range(rows):
#     matrix.append(input().split())
# for i in range(rows):
#     for j in range(cols - 1, -1, -1):
#         print(matrix[i][j], end=' ')
#     print()

# rows, cols = map(int, input().split())
# matrix = []
# for i in range(rows):
#     matrix.append(input().split())
# for i in range(rows - 1, -1, -1):
#     for j in range(cols):
#         print(matrix[i][j], end=' ')
#     print()

# rows, cols = map(int, input().split())
# matrix = []
# res1 = []
# res2 = [0]*cols
# for i in range(rows):
#     matrix.append(list(map(int, input().split())))
#     res1.append(sum(matrix[i]))
#     for j in range(cols):
#         res2[j] += matrix[i][j]
# print(*res1)
# print(*res2)

# n = int(input())
# matrix = []
# result = 'Yes'
# for i in range(n):
#     matrix.append(input().split())
# for i in range(n):
#     for j in range(n):
#         if matrix[i][j] != matrix[j][i]:
#             result = 'No'
#             break
#     if result == 'No':
#         break
# print(result)

# step 10
# rows, cols = map(int, input().split())
# max_summ = 0
# max_row = 0
# for i in range(rows):
#     summ = sum(map(int, input().split()))
#     if summ > max_summ:
#         max_summ = summ
#         max_row = i
# print(max_summ)
# print(max_row)

# step 11
# rows, cols = map(int, input().split())
# result = {'max_res': 0}
# for i in range(rows):
#     row = list(map(int, input().split()))
#     max_res = max(max(row), result['max_res'])
#     if max_res > result['max_res']:
#         result['max_res'] = max_res
#         result['row'] = i
#         result['col'] = row.index(max(row))
# print(result['max_res'])
# print(result['row'], result['col'])

# step 12
# rows, cols = map(int, input().split())
# max_shot = 0
# sum_shots = 0
# index_player = 0
# for i in range(rows):
#     row = list(map(int, input().split()))
#     max_shot_new = max(row)
#     sum_shots_new = sum(row)
#     if max_shot_new > max_shot:
#         max_shot = max_shot_new
#         sum_shots = sum_shots_new
#         index_player = i
#     elif max_shot_new == max_shot:
#         if sum_shots_new > sum_shots:
#             sum_shots = sum_shots_new
#             index_player = i
# print(index_player)

# step 13
# rows, cols = map(int, input().split())
# max_shot = 0
# max_shot_count = 0
# for i in range(rows):
#     row = list(map(int, input().split()))
#     max_shot_new = max(row)
#     if max_shot_new > max_shot:
#         max_shot = max_shot_new
#         max_shot_count = 1
#     elif max_shot_new == max_shot:
#         max_shot_count += 1
# print(max_shot_count)

# step 14
# m = []
# result = 'Yes'
# for _ in range(4):
#     m.append(list(input()))
#
# for i in range(3):
#     for j in range(3):
#         x = {m[i][j], m[i + 1][j], m[i][j + 1], m[i + 1][j + 1]}
#         if len(x) == 1:
#             result = 'No'
#             break
#     if result == 'No':
#         break
# print(result)

# step 15
# rows, cols = map(int, input().split())
# img = []
# result = 0
# for i in range(rows):
#     img.append(list(input()))
#
# input()
# for i in range(rows):
#     row = list(input())
#     for index, value in enumerate(row):
#         if value == img[i][index]:
#             result += 1
# print(result)

# step 16
