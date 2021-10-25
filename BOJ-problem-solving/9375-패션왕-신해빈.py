import collections

T = int(input())

for _ in range(T):
    n = int(input())
    wear = []
    for i in range(n):
        a, b = map(str, input().split())
        wear.append(b)
    num = 1
    result = collections.Counter(wear)
    for cnt in result:
        num *= (result[cnt]+1)
    print(num-1)

