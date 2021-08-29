M = int(input())
N = int(input())


def result(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


min_num = -1
sum_num = 0
for i in range(M, N + 1):
    if result(i):
        if min_num == -1:
            min_num = i
        sum_num += i

if min_num == -1:
    print(-1)
else:
    print(sum_num)
    print(min_num)
