"""
n, k = map(int, (input(), input()))
print(["YES", "NO", "Don't know"][(n >= k) + (n == k)])

print(['Равносторонний', 'Равнобедренный', 'Разносторонний'][len(set(map(int, (input() for _ in range(3))))) - 1])

x = map(int, (input() for _ in range(3)))
print(sorted(x)[1])
"""
x = int(input())
if x in (1, 3, 5, 7, 8, 10, 12):
    print(31)
elif x == 2:
    print(28)
else:
    print(30)
