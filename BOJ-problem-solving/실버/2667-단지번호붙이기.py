from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def solve(m, a, b):
    n = len(m)
    queue = deque()
    queue.append((a, b))
    m[a][b] = 0
    cnt = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if m[nx][ny] == 1:
                m[nx][ny] = 0
                queue.append((nx,ny))
                cnt += 1
    return cnt


N = int(input())
m = []
for _ in range(N):
    m.append(list(map(int, input())))

result = []
for i in range(N):
    for j in range(N):
        if m[i][j] == 1:
            result.append(solve(m, i, j))

print(len(result))
for i in sorted(result):
    print(i)
