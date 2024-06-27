'''
'# step 1
numbers = [(10, 10, 10), (30, 45, 56), (81, 39), (1, 2, 3), (12,), (-2, -4, 100), (1, 2, 99), (89, 9, 34),
           (10, 20, 30, -2), (50, 40, 50), (34, 78, 65), (-5, 90, -1, -5), (1, 2, 3, 4, 5, 6), (-9, 8, 4),
           (90, 1, -45, -21)]


def mean(data):
    return sum(data) / len(data)


print(min(numbers, key=mean))
print(max(numbers, key=mean))

# step 2
points = [(-1, 1), (5, 6), (12, 0), (4, 3), (0, 1), (-3, 2), (0, 0), (-1, 3), (2, 0), (3, 0), (-9, 1), (3, 6), (8, 8)]


def sort_func(point):
    return (point[0] ** 2 + point[1] ** 2) ** 0.5


points.sort(key=sort_func)
print(points)
'''
# step 3
numbers = [(10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3), (12, 45, 67), (-2, -4, 100), (1, 2, 99), (89, 90, 34),
           (10, 20, 30), (50, 40, 50), (34, 78, 65), (-5, 90, -1)]


def sort_func(data):
    return min(data) + max(data)


numbers.sort(key=sort_func)
print(numbers)
