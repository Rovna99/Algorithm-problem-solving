import sys

N = int(sys.stdin.readline())
score = list(map(int, sys.stdin.readline().split()))
max_s = max(score)
aver = 0
for i in range(N):
    score[i] = score[i] / max_s * 100
    aver += score[i]

aver /= N

print(aver)
