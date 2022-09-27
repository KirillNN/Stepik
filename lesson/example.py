from time import sleep


def sleep_for(seconds: int):
    sleep(seconds)


def is_smaller(num1: int, num2: int):
    return num1 < num2


def get_max_n2(nums: list):
    N = len(nums)
    maxi = float('-inf')
    for i in range(N):
        is_max = True
        for j in range(N):
            if is_smaller(nums[i], nums[j]):
                is_max = False
        if is_max:
            maxi = nums[i]
    return maxi


def get_max_n(nums: list):
    maxi = float('-inf')
    for num in nums:
        maxi = max(maxi, num)


array = [x for x in range(1000)]

# sleep_for(1)
print(get_max_n(array))

# sleep_for(2)
print(get_max_n(array))
