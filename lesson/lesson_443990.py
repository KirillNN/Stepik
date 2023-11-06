"""
# step 9
n = int(input())
data = []
for _ in range(n):
    data.append(input())

for i in data:
    print(i)

print()
for i in data:
    if '4' in i or '5' in i:
        print(i)

# step 15
tribo = [1, 1, 1]
n = int(input())
if n <= 3:
    print(*tribo[:n])
else:
    for i in range(n - 3):
        tribo.append(sum(tribo[i:i + 4]))
    print(*tribo)
"""

tpl = (100, 200, 300, 400, 500)
print(tpl[-2])
print(tpl[-4:-1])