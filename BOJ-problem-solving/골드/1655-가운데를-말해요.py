import heapq
import sys

n = int(sys.stdin.readline())
b = []
s = []
for i in range(n):
    x = int(sys.stdin.readline())
    if len(s) == len(b):
        heapq.heappush(s, -x)
    else:
        heapq.heappush(b, x)
    if not b:
        print(-s[0])
        continue
    if -s[0] > b[0]:
        n = -heapq.heappop(s)
        m = heapq.heappop(b)
        heapq.heappush(s, -m)
        heapq.heappush(b, n)
    print(-s[0])
