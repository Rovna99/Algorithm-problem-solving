# 첫 시도.
import sys

n = int(sys.stdin.readline())
num = []
for i in range(n):
    a = sys.stdin.readline().strip()
    num.append([a, len(a)])

num.sort(key=lambda x: (x[1], x[0]))
result = []

for i in range(len(num)):
    if num[i][0] not in result:
        result.append(num[i][0])
        print(num[i][0])

# 더 간결하고 시간 복잡도, 메모리가 더 빠른 코드

n = int(sys.stdin.readline())
num = []

for i in range(n):
    num.append(sys.stdin.readline().strip())

set_num = set(num)
num = list(set_num)

num.sort()
num.sort(key=len)

for i in num:
    print(i)

