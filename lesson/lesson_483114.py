"""
# step 8
set1 = set(input())
set2 = set(input())
print('NO' if set1.isdisjoint(set2) else 'YES')

# step 9
set1 = set(input())
set2 = set(input())
print('YES' if set2.issubset(set1) else 'NO')

# step 10
set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))
set3 = set(map(int, input().split()))
print(*sorted(set1 & set2 - set3, reverse=True))

# step 11
set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))
set3 = set(map(int, input().split()))
print(*sorted((set1 | set2 | set3) - (set1 & set2 & set3)))

# step 12
set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))
set3 = set(map(int, input().split()))
set3 -= (set1 | set2)
print(*sorted(set3, reverse=True))
"""
# step 13
set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))
set3 = set(map(int, input().split()))
result = set(range(11))
print(*sorted(result - set1 - set2 - set3))
