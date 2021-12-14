import sys

T = int(sys.stdin.readline())
for _ in range(T):
    K = int(sys.stdin.readline())
    p = list(map(int, sys.stdin.readline().split()))
    dp = [[0]*K for _ in range(K)]

    for i in range(K-1):
        dp[i][i+1] = p[i] + p[i+1]
        for j in range(i+2, K):
            dp[i][j] = dp[i][j-1] + p[j]

    for d in range(2, K):
        for i in range(K-d):
            j = i+d
            minimum = [dp[i][K] + dp[K+1][j] for K in range(i, j)]
            dp[i][j] += min(minimum)

    print(dp[0][K-1])
