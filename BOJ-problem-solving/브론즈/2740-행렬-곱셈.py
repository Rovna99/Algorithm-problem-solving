N, M = map(int, input().split())
A = []

for i in range(N):
    A.append(list(map(int, input().split())))

M, K = map(int, input().split())
B = []

for i in range(M):
    B.append(list(map(int, input().split())))

result = [[0 for _ in range(K)] for _ in range(N)]

for n in range(N):
    for k in range(K):
        for m in range(M):
            result[n][k] += A[n][m] * B[m][k]
# [[sum([A[n][m] * B[m][k] for m in range(M)]) for k in range(K)] for n in range(N)]

for i in result:
    print(*i)

