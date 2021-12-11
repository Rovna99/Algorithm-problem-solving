def dfs(start):
    global cnt
    visited[start] = 1
    for i in graph[start]:
        if visited[i] == 0:
            dfs(i)
            cnt += 1


c = int(input())
n = int(input())
graph = [[] for _ in range(c+1)]

for i in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (c+1)
cnt = 0

dfs(1)
print(cnt)