import sys

max_n = 123456
max_li = [True] * (max_n * 2 + 1)

for i in range(2, int((2 * max_n) ** 0.5) + 1):
    if max_li[i]:
        for j in range(2 * i, 2 * max_n + 1, i):
            max_li[j] = False

while True:
    n = int(sys.stdin.readline().rstrip())

    if n == 0:
        break

    result = max_li[n + 1: 2 * n + 1]
    print(result.count(True))
