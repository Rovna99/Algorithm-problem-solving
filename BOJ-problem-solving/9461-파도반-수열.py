dp = [0 for i in range(101)]
dp[1], dp[2], dp[3] = 1, 1, 1
for spiral in range(4, 101):
    dp[spiral] = dp[spiral-2] + dp[spiral-3]
# 1일때 1, 2일때 1, 3일때 1, 4일때 2, 5일때 2,  즉, n = (n-2)+ (n-3)

N = int(input())
for i in range(N):
    print(dp[int(input())])
