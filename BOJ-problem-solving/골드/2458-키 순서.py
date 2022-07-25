import sys

n, m = map(int, sys.stdin.readline().split())
count = 0

big = [set() for _ in range(n + 1)]
small = [set() for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    big[a].add(b)
    small[b].add(a)

for i in range(1, n+1):
    for j in big[i]:
        small[j].update(small[i])
    for j in small[i]:
        big[j].update(big[i])

for i in range(1, n+1):
    if len(big[i]) + len(small[i]) == n-1:
        count += 1

print(count)
