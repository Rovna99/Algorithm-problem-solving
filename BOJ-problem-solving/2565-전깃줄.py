N = int(input())
dp = [1 for i in range(N)]
line = []
for i in range(N):
    line.append(list(map(int, input().split())))

line.sort()

for i in range(N):
    for j in range(i):
        if line[i][1] > line[j][1] and dp[i] < dp[j]+1:
            dp[i] = dp[j]+1

print(N-max(dp))
