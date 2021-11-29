import sys

K, N = map(int, sys.stdin.readline().split())
k = [int(sys.stdin.readline()) for _ in range(K)]

start, end = 1, 2**32

while start < end:
    mid = (start + end) // 2
    line = 0
    for i in k:
        line += i // mid

    if line >= N:
        start = mid + 1
    else:
        end = mid


print(end-1)
