# 산술평균 : N개의 수들의 합을 N으로 나눈 값
# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값
# 범위 : N개의 수들 중 최댓값과 최솟값의 차이
from collections import Counter
import sys

num = []
for i in range(int(sys.stdin.readline())):
    num.append(int(sys.stdin.readline()))

num.sort()
print(round(sum(num)/len(num)))#산술평균
print(num[len(num)//2])#중앙값

cnt = Counter(num).most_common()#최빈값
max_n = cnt[0][1]
result = []
for n in cnt:
    if n[1] == max_n:
        result.append(n[0])
if len(result) > 1:
    print(result[1])
else:
    print(result[0])
print(max(num)-min(num))#범위
