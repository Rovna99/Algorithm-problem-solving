import heapq
import sys

N = int(sys.stdin.readline())
q = []
for i in range(N):
    x = int(sys.stdin.readline())

    if not x:
        if not len(q):
            print(0)
        else:
            print(heapq.heappop(q)[1])

    else:
        heapq.heappush(q, [abs(x), x])
