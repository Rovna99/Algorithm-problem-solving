import sys
from collections import deque

N = int(sys.stdin.readline())

n_list = deque([_ for _ in range(1, N+1)])


while len(n_list) != 1:
    n_list.popleft()
    n_list.append(n_list.popleft())

print(n_list[-1])

