import sys

A, B, C = map(int, sys.stdin.readline().rstrip().split())


def cut(a, b):
    if b == 1:
        return a % C
    else:
        x = cut(a, b//2)
        if b % 2 == 0:
            return x * x % C
        else:
            return x * x * a % C


print(cut(A, B))

