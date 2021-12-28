T = int(input())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def solve(x, y):
    queue = [[x, y]]
    while queue:
        a, b = queue[0][0], queue[0][1]
        del queue[0]
        for i in range(4):
            q = a + dx[i]
            w = b + dy[i]
            if 0 <= q < N and 0 <= w < M and farm[q][w] == 1:
                farm[q][w] = 0
                queue.append([q, w])


for i in range(T):
    M, N, K = map(int, input().split())
    farm = [[0] * M for _ in range(N)]
    cnt = 0
    for j in range(K):
        x, y = map(int, input().split())
        farm[y][x] = 1

    for q in range(N):
        for w in range(M):
            if farm[q][w] == 1:
                solve(q, w)
                farm[q][w] = 0
                cnt += 1
    print(cnt)
