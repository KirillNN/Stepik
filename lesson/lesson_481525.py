# step 6
numbers = {1.414, 12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324, 2.718, 1.324}

print(min(numbers) + max(numbers))

# step 7
numbers = {20, 6, 8, 18, 18, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 12, 8, 8, 10, 4, 2, 2, 2, 16, 20}
average = sum(numbers) / len(numbers)

print(average)

# step 10
numbers = {9089, -67, -32, 1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111, 111, 1, 23}

print(sum([x ** 2 for x in numbers]))

# step 11
fruits = {'apple', 'banana', 'cherry', 'avocado', 'pineapple', 'apricot', 'banana', 'avocado', 'grapefruit'}

print(*sorted(fruits, reverse=True), sep='\n')

# step 12
print(len(set(input())))

# step 13
text = input()
print('YES' if len(set(text)) == len(text) else 'NO')

print('YES' if len(s := input()) == len(set(s)) else 'NO')

# step 14
print('YES' if len(set(input() + input())) == 10 else 'NO')

# step 15
print('YES' if set(input()) == set(input()) else 'NO')

# step 16
a, b, c = map(set, input().split())
print('YES' if a == b == c else 'NO')
