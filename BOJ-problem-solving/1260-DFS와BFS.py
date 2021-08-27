from collections import deque

n, m, s = map(int, input().split())

graph = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    m1, m2 = map(int, input().split())
    graph[m1][m2] = graph[m2][m1] = 1


def dfs(s, discoverd=[]):
    discoverd.append(s)
    print(s, end=' ')

    for w in range(len(graph[s])):
        if graph[s][w] == 1 and (w not in discoverd):
            dfs(w, discoverd)


def bfs(s):
    discoverd = [s]
    queue = deque()
    queue.append(s)

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for w in range(len(graph[s])):
            if graph[v][w] == 1 and (w not in discoverd):
                discoverd.append(w)
                queue.append(w)


dfs(s)
print()
bfs(s)
