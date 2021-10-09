
one = list(input())
two = list(input())
o_l = len(one)
t_l = len(two)
dp = [[0]*(t_l+1) for _ in range(o_l+1)]

for i in range(o_l):
    for j in range(t_l):
        if one[i] == two[j]:
            dp[i + 1][j + 1] = dp[i][j] + 1
        else:
            dp[i + 1][j + 1] = max(dp[i][j+1], dp[i+1][j])

print(dp[o_l][t_l])
