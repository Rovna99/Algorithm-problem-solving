import sys

input = sys.stdin.readline
N = int(input())
drink = [0] + [int(input()) for _ in range(N)]
dp = [0, drink[1]] + [0 for _ in range(N-1)]

if N > 1:
    dp[2] = drink[1]+drink[2]

for i in range(3, N+1):
    dp[i] = max(dp[i-1], drink[i]+drink[i-1] + dp[i-3], drink[i]+dp[i-2])

print(dp[N])
