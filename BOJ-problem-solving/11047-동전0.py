N, K = map(int, input().split())
money = []
for _ in range(N):
    money.append(int(input()))

cnt = 0
for i in range(N - 1, -1, -1):
    if K == 0:
        break
    if K >= i:
        cnt += (K // money[i])
        K %= money[i]

print(cnt)
