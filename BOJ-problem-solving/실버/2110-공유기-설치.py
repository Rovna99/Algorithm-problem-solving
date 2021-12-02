import sys

N, C = map(int, sys.stdin.readline().rstrip().split())
x = sorted([int(sys.stdin.readline().rstrip()) for i in range(N)])


start = 1
end = (x[-1] - x[0]) // (C-1)
result = 0
while start <= end:
    mid = (start + end) // 2
    current = x[0]
    cnt = 1

    for i in x:
        if i >= current + mid:
            cnt += 1
            current = i

    if cnt >= C:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)
