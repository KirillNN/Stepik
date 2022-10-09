"""
mult = 1
for i in range(1, 11):
   if i % 2 == 0:
      continue
   if i % 9 == 0:
      break
   mult *= i
print(mult)

n = int(input())
count = 2
while n >= count:
    if not n % count:
        print(count)
        break
    count += 1

n = int(input())
count = 1
while count <= n:
    if count not in range(5, 10) and count not in range(17, 38) and count not in range(78, 88):
        print(count)
    count += 1
"""
n = 0
while n < 10:
    n += 2
    print(n)
else:
    print('Цикл завершен.')
