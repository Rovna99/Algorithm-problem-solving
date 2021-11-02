import sys

N = int(sys.stdin.readline())
stack = list(map(int, sys.stdin.readline().rstrip().split()))
result = [-1] * N
idx = [0]

for i in range(1, N):
    while idx and stack[idx[-1]] < stack[i]:
        result[idx.pop()] = stack[i]
    idx.append(i)

for i in result:
    print(i, end=' ')

