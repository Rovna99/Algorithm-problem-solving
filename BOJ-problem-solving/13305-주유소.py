N = int(input())
dist = list(map(int, input().split()))
oil = list(map(int, input().split()))

min_m = oil[0]
result = 0
for i in range(N-1):
    if oil[i] < min_m:
        min_m = oil[i]

    result += min_m * dist[i]

print(result)
