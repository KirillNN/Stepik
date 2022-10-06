"""
total = 0
for i in range(1, 6):
    total += i
    print(total, end='')

a, b = map(int, (input() for _ in range(2)))
count = 0
for i in range(a, b + 1):
    if i ** 3 % 10 == 4 or i ** 3 % 10 == 9:
        count += 1
print(count)

ar = map(int, (input() for _ in range(int(input()))))
print(sum(ar))

from math import log

n = int(input())
exp = 0
for i in range(1, n + 1):
    exp += 1 / i
exp -= log(n)
print(exp)

n = int(input())
count = 0
for i in range(1, n + 1):
    x = i ** 2 % 10
    if x in (2, 5, 8):
        count += i
print(count)

from math import factorial

n = int(input())
print(factorial(n))

multi = 1
for _ in range(10):
    x = int(input())
    if x:
        multi *= x
print(multi)

n = int(input())
summ = 0
for i in range(1, n + 1):
    if not n % i:
        summ += i
print(summ)

n = int(input())
summ = 0
for i in range(1, n + 1):
    summ += (-1) ** (i - 1) * i
print(summ)

ar = list(map(int, (input() for _ in range(int(input())))))
ar.sort(reverse=True)
print(*ar[:2], sep='\n')

res = 'YES'
for _ in range(10):
    x = int(input())
    if x % 2:
        res = 'NO'
print(res)
"""
n = int(input())
if n == 1:
    print(1)
elif n == 2:
    print(1, 1)
else:
    res = [1, 1]
    for i in range(0, n - 2):
        res.append(sum(res[i:i + 2]))
    print(*res)
