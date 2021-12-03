import sys

N = int(sys.stdin.readline())
k = int(sys.stdin.readline())

start, end = 1, k
while start <= end:

    mid = (start + end) // 2

    B = 0
    for i in range(1, N+1):
        B += min(mid//i, N)

    if B >= k:
        result = mid
        end = mid - 1
    else:
        start = mid + 1
print(result)

