# step 7

ip = map(int, input().split('.'))

for item in ip:
    if item <0 or item > 255:
        print('НЕТ')
        break
else:
    print('ДА')