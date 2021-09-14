import sys

input = sys.stdin.readline
num = []
for _ in range(int(input())):
    a, b = map(int, input().split())
    num.append([a, b])

num.sort(key=lambda x: (x[1], x[0]))

for a, b in num:
    print(a, b)
