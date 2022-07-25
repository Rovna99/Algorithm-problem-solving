from collections import deque
import sys
input = sys.stdin.readline
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]


def solve(cx, cy, fx, fy):
    q = deque()
    q.append([cx, cy])
    board[cx][cy] = 1
    while q:
        a, b = q.popleft()
        if a == fx and b == fy:
            print(board[fx][fy]-1)
            return
        for i in range(8):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < I and 0 <= y < I and board[x][y] == 0:
                q.append([x, y])
                board[x][y] = board[a][b] + 1


T = int(input())
for _ in range(T):
    I = int(input())

    cx, cy = map(int, input().split())
    fx, fy = map(int, input().split())
    board = [[0] * I for _ in range(I)]
    solve(cx, cy, fx, fy)

