from itertools import *
# 내 풀이
N = int(input())

cnt = 0
six_3 = 666
while True:
    if '666' in str(six_3):
        cnt += 1
    if cnt == N:
        print(six_3)
        break
    six_3 += 1

# 문제에서 원한 브루트 포스는 아니지만 최적화가 엄청 잘된 코드..

N = int(input())
nums = []
for k in range(1, 5):
    nums.extend(map(list, product(map(str, range(10)), repeat=k)))
title = [666]
for l in nums:
    for i in range(len(l) + 1):
        title.append(int(''.join(l[:i] + ['666'] + l[i:])))
title = list(set(title))
title.sort()
print(title[N - 1])
