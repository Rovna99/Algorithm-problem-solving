import sys

N = int(input())

for _ in range(N):
    a, b = map(int, sys.stdin.readline().strip().split())
    a2, b2 = a, b

    while a % b != 0:
        a, b = b, a % b

    print(a2 * b2 // b)


