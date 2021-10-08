N = int(input())

lst = list(map(int, input().split()))
reverse_lst = lst[::-1]

up = [1 for _ in range(N)]
down = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if lst[i] > lst[j]:
            up[i] = max(up[i], up[j]+1)
        if reverse_lst[i] > reverse_lst[j]:
            down[i] = max(down[i], down[j]+1)

result = [0 for _ in range(N)]

for i in range(N):
    result[i] = up[i] + down[N-i-1] - 1

print(max(result))
