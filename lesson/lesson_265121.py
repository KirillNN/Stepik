"""
ar = []
while True:
    text = input()
    if text != 'КОНЕЦ':
        ar.append(text)
    else:
        break
print(*ar, sep='\n')

ar = []
while True:
    text = input()
    if text.upper() != 'КОНЕЦ':
        ar.append(text)
    else:
        break
print(*ar, sep='\n')

count = 0
while True:
    text = input()
    if text in ['стоп', 'хватит', 'достаточно']:
        break
    count += 1
print(count)

ar = []
while True:
    n = int(input())
    if n % 7:
        break
    ar.append(n)
print(*ar, sep='\n')

ar = []
while True:
    n = int(input())
    if n < 0:
        break
    ar.append(n)
print(sum(ar))

count = 0
while True:
    n = int(input())
    if n < 0 or n > 5:
        break
    if n == 5:
        count += 1
print(count)
"""
n = int(input())
count = 0
while n:
    for i in (25, 10, 5, 1):
        if n >= i:
            count += 1
            n -= i
            break
print(count)
