"""
n, m = int(input()), int(input())

my_list = [[0] * m ] * n
print(my_list)
my_list[0][0] = 17

print(my_list)
"""
# step 8
n = int(input())
list = []
for _ in range(n):
    list.append([x for x in range(1, n + 1)])

print(*list, sep='\n')
