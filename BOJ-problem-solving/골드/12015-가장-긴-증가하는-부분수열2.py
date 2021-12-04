import sys
from bisect import bisect_left

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))


def LIS(a):
    ans = [a[0]]
    for i in a[1:]:
        if i > ans[-1]:
            ans.append(i)
        else:
            ans[bisect_left(ans, i)] = i
    return len(ans)


print(LIS(A))

# 정석
# result = [0]
#
# for i in A:
#     if result[-1] < i:
#         result.append(i)
#     else:
#         start = 0
#         end = len(result)
#
#         while start < end:
#             mid = (start + end) // 2
#
#             if result[mid] < i:
#                 start = mid + 1
#             else:
#                 end = mid
#         result[end] = i
#
# print(len(result)-1)

