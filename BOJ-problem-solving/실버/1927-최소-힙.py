import heapq
import sys

N = int(sys.stdin.readline())
result = []
for i in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if not result:
            print(0)
        else:
            print(heapq.heappop(result))
    else:
        heapq.heappush(result, x)
