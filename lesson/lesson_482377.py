"""
# step 13
set1 = set(input().split())
set2 = set(input().split())
print(len(set1 & set2))

# step 14
set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))
print(*sorted(set1 & set2))

# step 15
set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))
print(*sorted(set1 - set2))
"""
# step 16
n = int(input())
numbers = set(input())
for _ in range(n - 1):
    numbers &= set(input())
print(*sorted(numbers))
