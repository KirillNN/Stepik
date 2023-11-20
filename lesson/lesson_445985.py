"""
# step 2
n, m, k, p = [int(input()) for i in range(4)]
print(n - m + p - k)

# step 3
n = input().split()
print(len(n) - len(set(n)))

# step 4
n = int(input())
words = {input() for _ in range(n + 1)}
print('OK' if len(words) == n + 1 else 'REPEAT')

# step 5
m = int(input())
n = int(input())
set_m = set()
for _ in range(m):
    set_m.add(input())

list_n = []
for _ in range(n):
    list_n.append(input())

for i in list_n:
    print('YES' if i in set_m else 'NO')

# step 6
n = set(map(int, input().split()))
m = set(map(int, input().split()))
if len(n & m) == 0:
    print('BAD DAY')
else:
    print(*sorted(n & m, reverse=True))

n = set(map(int, input().split()))
m = set(map(int, input().split()))
print('BAD DAY' if len(n & m) == 0 else ' '.join(map(str, sorted(n & m, reverse=True))))

# step 7
n = set(input().split())
m = set(input().split())
print('YES' if n == m else 'NO')

# step 8
m = int(input())
n = int(input())
set_m = set()
for _ in range(m):
    set_m.add(input())

set_n = set()
for _ in range(n):
    set_n.add(input())

print(len(set_m - set_n))

# step 9
m = int(input())
n = int(input())
set_m = set()
for _ in range(m):
    set_m.add(input())

set_n = set()
for _ in range(n):
    set_n.add(input())

result = len(set_m ^ set_n)
print(result if result > 0 else 'NO')

# step 10
n = set(input().split())
m = set(input().split())
n |= m
print(*sorted(n))

# step 11
m, n = int(input()), int(input())
set_all = {input() for _ in range(m + n)}
print(['NO', 2 * len(set_all) - (m + n)][2 * len(set_all) != m + n])
"""
# step 12
n = int(input())
result = {input() for _ in range(int(input()))}

for _ in range(n - 1):
    result &= {input() for _ in range(int(input()))}

print(*sorted(result), sep='\n')