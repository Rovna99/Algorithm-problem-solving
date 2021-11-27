import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
A.sort()
M = int(input())
M_list = list(map(int, input().split()))


def b_search(t):
    l = 0
    r = N - 1
    while l <= r:
        m = (l + r) // 2

        if A[m] == t:
            return True

        if t < A[m]:
            r = m - 1
        elif t > A[m]:
            l = m + 1


for i in range(M):
    if b_search(M_list[i]):
        print(1)
    else:
        print(0)
