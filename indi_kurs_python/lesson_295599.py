# t = 0
# z = 50
# d = z - 15
# z = 2 * d
# t = z - 40
# print(t)
#
# p = 5
# y = 7
# w = p + y
# w = w + 1
# p = y
# y = 10
# p = 2 + w + y
# print(p)
#
# year = int(input())
# print(year + 1)
#
# n = int(input())
# print(n * 2)
# print(n / 2)
#
# n = float(input())
# print(n ** 2)
#
# a = int(input())
# b = int(input())
# print(a + b)
#
# a = float(input())
# b = float(input())
# print(a * b, 2 * a + 2 * b)
#
# f = float(input())
# print((f - 32) * 5 / 9)

# a = int(input())
# b = int(input())
# print(abs(a) + abs(b))
#
# x1 = float(input())
# x2 = float(input())
# print(max(x1, x2) - min(x1, x2))
#
# x1 = float(input())
# print(round(x1, 2), round(x1, 3))

x1, x2, x3, y1, y2, y3 = map(int, (input() for _ in range(6)))
print((y1 - x1) * 3600 + (y2 - x2) * 60 + (y3 - x3))
