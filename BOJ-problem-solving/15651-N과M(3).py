from itertools import product
import sys

N, M = map(int, input().split())
result = []

# 라이브러리 x
def NaM():
    if len(result) == M:
        print(' '.join(map(str, result)))
        return

    for i in range(1, N+1):
        result.append(i)
        NaM()
        result.pop()


NaM()
# itertools 사용


input = sys.stdin.readline

N, M = list(map(int,input().split()))
arr = list(map(str,range(1,N+1)))
for i in list(product(arr,repeat=M)):
    print(' '.join(i))
