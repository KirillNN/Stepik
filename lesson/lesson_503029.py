# step 16
def matrix(n=1, m=None, value=0):
    return [[value] * m if m else [value] * n for _ in range(n)]


print(matrix())
print(matrix(3))
print(matrix(2, 5))
print(matrix(3, 4, 9))
