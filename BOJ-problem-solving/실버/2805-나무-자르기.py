import sys

N, M = map(int, sys.stdin.readline().split())
T = sorted(list(map(int, sys.stdin.readline().split())))


def check(m):
    s = 0
    for i in T:
        if i > mid:
            c = i - mid
            s += c
    if s >= M:
        return True
    else:
        return False


start = 0
end = max(T)
while start + 1 < end:
    mid = (start + end) // 2

    if check(mid):
        start = mid
    else:
        end = mid

print(start)


