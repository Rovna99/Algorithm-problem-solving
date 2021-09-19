import sys

n = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().split()))

x1 = sorted(list(set(x)))# xi > xj 의 갯수는 정렬한 자리의 순서와 같음.

result = {x1[i]: i for i in range(len(x1))}

for i in x:
    print(result[i], end=' ')

