import sys

N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
for i in range(1, len(num)):
    num[i] += num[i-1] if num[i-1] > 0 else 0
print(max(num))

