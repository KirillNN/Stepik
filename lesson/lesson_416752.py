"""
# step 12
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)


list2 = [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]

print(list1==list2)

# step 13
list1 = ['a', 'b', ['c', ['d', 'e', ['f', 'g'], 'k'], 'l'], 'm', 'n']
sub_list = ['h', 'i', 'j']
list1[2][1][2].extend(sub_list)
list2 = ['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']

print(list1==list2)

# step 14
list1 = [[1, 7, 8], [9, 7, 102], [6, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
maximum = -1
for i in list1:
    if max(i) > maximum:
        maximum = max(i)
print(maximum)

# step 15
list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
list1 = [x[::-1] for x in list1]
print(list1)

list2 = [[8, 7, 1], [102, 7, 9], [105, 106, 102], [103, 98, 99, 100], [3, 2, 1]]
print(list1 == list2)
"""
# step 16
list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
total = sum(map(sum, [x for x in list1]))
counter = sum(map(len, [x for x in list1]))
print(total / counter)
