import sys


# def factorial(f):
#     num = 1
#     for i in range(f):
#         num *= (i+1)
#     return num
#
#
# N, K = map(int, sys.stdin.readline().rstrip().split())
#
# n = factorial(N)
# k = factorial(N-K)*factorial(K)
# print((n//k) % 10007)

N, K = map(int, sys.stdin.readline().rstrip().split())
dp = [[0] * 1 for _ in range(1002)]
dp[1].append(1)
for i in range(2, 1002):
    for j in range(1, i + 1):
        if j == 1 or j == i:
            dp[i].append(1)
        else:
            dp[i].append(dp[i - 1][j - 1] + dp[i - 1][j])

print(dp[N + 1][K + 1] % 10007)

