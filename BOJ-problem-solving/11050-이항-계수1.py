import sys

N, K = map(int, sys.stdin.readline().rstrip().split())


def bc(f):
    num = 1
    for i in range(f):
        num *= (i+1)
    return num


n = bc(N)
k = bc(N-K)*bc(K)

print(n//k)
