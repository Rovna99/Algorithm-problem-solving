import sys

T = int(input())

for _ in range(T):
    s = sys.stdin.readline().rstrip()
    score = 0
    streak = 0
    for ox in s:
        if ox == 'O':
            streak += 1
            score += streak
        elif ox == 'X':
            streak = 0
    print(score)
