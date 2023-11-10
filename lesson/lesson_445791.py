# step 11
# print(*[len(set(input().lower())) for _ in range(int(input()))], sep='\n')

# step 12
# print(len(set(''.join(input().lower() for _ in range(int(input()))))))

# step 13
# text = input()
# result = set(map(lambda x: x.lower().strip('.,;:-?!'), text.split()))
# print(len(result))

# step 14
numbers = list(map(int, input().split()))

for index, value in enumerate(numbers):
    if value in numbers[:index]:
        print('YES')
    else:
        print('NO')