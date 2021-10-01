import sys

input = sys.stdin.readline
N = int(input())
dp = []
for _ in range(N):
    dp.append(list(map(int, input().split())))

index = 2
for i in range(1, N):
    for j in range(index):
        if j == 0:
            dp[i][j] = dp[i][j] + dp[i-1][j]
        elif i == j:
            dp[i][j] = dp[i][j] + dp[i-1][j-1]
        else:
            dp[i][j] = max(dp[i][j]+dp[i-1][j], dp[i][j]+dp[i-1][j-1])
    index += 1
print(max(dp[N-1]))
