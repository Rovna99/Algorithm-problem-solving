import sys

n, k = map(int, sys.stdin.readline().split())
m = []
dp = [0 for i in range(k+1)]
dp[0] = 1
for i in range(n):
    m.append(int(sys.stdin.readline()))
m.sort()
for i in m:
    for j in range(i, k+1):
        dp[j] += dp[j - i]

print(dp[k])
