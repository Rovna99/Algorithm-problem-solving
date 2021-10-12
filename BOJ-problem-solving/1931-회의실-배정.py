import sys

N = int(sys.stdin.readline())
lst = []
for _ in range(N):
    lst
    lst.append(list(map(int, sys.stdin.readline().split())))

lst.sort(key=lambda x: x[0])
lst.sort(key=lambda x: x[1])

m_end = 0
cnt = 0
for start, end in lst:
    if m_end <= start:
        cnt += 1
        m_end = end

print(cnt)
