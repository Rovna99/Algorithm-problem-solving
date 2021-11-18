import sys

N = int(input())
p = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
result = []


def cut(x, y, N):
    color = p[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if color != p[i][j]:
                cut(x, y, N//2)
                cut(x, y+N//2, N//2)
                cut(x+N//2, y, N//2)
                cut(x+N//2, y+N//2, N//2)
                return
    if color == 0:
        result.append(0)
    else:
        result.append(1)


cut(0, 0, N)
print(result.count(0))
print(result.count(1))
