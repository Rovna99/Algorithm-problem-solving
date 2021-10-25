import sys

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    wear = {}
    for _ in range(n):
        a, b = sys.stdin.readline().split()
        if b in wear:
            wear[b] += 1
        else:
            wear[b] = 1
    num = 1
    for k, v in wear.items():
        num *= (v+1)
    print(num-1)

