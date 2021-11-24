N, B = map(int, input().split())
num = [list(map(int, input().split())) for _ in range(N)]


def solve(a, b):
    if b == 1:
        for i in range(N):
            for j in range(N):
                a[i][j] %= 1000
        return a
    elif b % 2 == 1:
        tmp = [[0 for _ in range(N)] for _ in range(N)]
        arr2 = solve(a, b-1)
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    tmp[i][j] += arr2[i][k]*a[k][j]
                tmp[i][j] %= 1000
        return tmp
    else:
        tmp = [[0 for _ in range(N)] for _ in range(N)]
        arr2 = solve(a, b//2)
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    tmp[i][j] += arr2[i][k] * arr2[k][j]
                tmp[i][j] %= 1000
        return tmp


result = solve(num, B)
for i in result:
    print(*i)
