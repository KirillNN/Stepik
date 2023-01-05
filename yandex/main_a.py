n = int(input())
a = list(map(int, input().split()))

for i, j in zip(a[:], a[1:]):
    if i > j:
        print(-1)
        break
else:
    print(a[-1] - a[0])
