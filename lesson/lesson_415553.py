# step 7
# number = input()
#
# print(int(number[::-1]) if len(number) == 5 else int(number[0] + number[:0:-1]))


# step 8
# number = int(input())
# print(f"{number:,d}")

# step 10
n, k = int(input()), int(input())

peoples = list(range(1, n + 1))
kill = 0
while len(peoples) > 1:
    kill = (kill - 1 + k) % len(peoples)
    peoples.pop(kill)

print(*peoples)
