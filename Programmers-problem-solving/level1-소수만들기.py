import itertools


def sosu(n):
    if n < 2 or n % 2 == 0:
        return False
    if n == 2 or n == 3:
        return True
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def solution(nums):
    result = []
    cnt = 0
    nums3 = itertools.combinations(nums, 3)

    for i in nums3:
        result.append(sum(i))

    for i in result:
        if sosu(i):
            cnt += 1
    return cnt
