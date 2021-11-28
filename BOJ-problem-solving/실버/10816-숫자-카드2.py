import sys

_ = int(sys.stdin.readline())
N = sorted(map(int, sys.stdin.readline().split()))
_ = int(sys.stdin.readline())
M = list(map(int, sys.stdin.readline().split()))


def b_s(n, N, start, end):
    if start > end:
        return 0
    m = (start+end)//2

    if n == N[m]:
        return N[start:end+1].count(n)
    elif n < N[m]:
        return b_s(n, N, start, m-1)
    else:
        return b_s(n, N, m+1, end)


result = {}

for n in N:
    s = 0
    e = len(N) - 1
    if n not in result:
        result[n] = b_s(n, N, s, e)

print(' '.join(str(result[x]) if x in result else '0' for x in M))


# 해쉬 방식
# from sys import stdin
# _ = stdin.readline()
# N = map(int,stdin.readline().split())
# _ = stdin.readline()
# M = map(int,stdin.readline().split())
# hashmap = {}
# for n in N:
#     if n in hashmap:
#         hashmap[n] += 1
#     else:
#         hashmap[n] = 1
#
# print(' '.join(str(hashmap[m]) if m in hashmap else '0' for m in M))

#counter
# from sys import stdin
# from collections import Counter
# _ = stdin.readline()
# N = stdin.readline().split()
# _ = stdin.readline()
# M = stdin.readline().split()
#
# C = Counter(N)
# print(' '.join(f'{C[m]}' if m in C else '0' for m in M))
