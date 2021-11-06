import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
num = deque([])
for i in range(1, N+1):
    num.append(i)
print('<', end='')
while num:
    for _ in range(K - 1):
        num.append(num.popleft())
    print(num.popleft(), end='')

    if num:
        print(', ', end='')
print('>')
