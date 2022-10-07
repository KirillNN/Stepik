"""
num = 123456789
total = 0
while num != 0:
    last_digit = num % 10
    if last_digit > 4:
        total += 1
    num = num // 10
print(total)

n = int(input())
while n:
    print(n % 10)
    n //= 10

print(input()[::-1])

n = int(input())
d_max = 0
d_min = 9
while n:
    if n % 10 < d_min:
        d_min = n % 10
    if n % 10 > d_max:
        d_max = n % 10
    n //= 10
print(f'Максимальная цифра равна {d_max}')
print(f'Минимальная цифра равна {d_min}')

n = int(input())
d_sum = 0
d_count = 0
d_multi = 1
d_last_flag = True
while n:
    x = n % 10
    d_first = x
    if d_last_flag:
        d_last = x
        d_last_flag = False
    d_count += 1
    d_sum += x
    d_multi *= x
    n //= 10
print(d_sum)
print(d_count)
print(d_multi)
print(d_sum / d_count)
print(d_first)
print(d_first + d_last)

print(input()[1])

n = input()
res = 'NO'
if len(set(n)) == 1:
    res = 'YES'
print(res)
"""
n = int(input())
res = 'YES'
last = 0
while n:
    first = n % 10
    if first < last:
        res = 'NO'
    last = first
    n //= 10
print(res)
