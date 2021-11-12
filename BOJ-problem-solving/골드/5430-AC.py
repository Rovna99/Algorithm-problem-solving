import sys
from collections import deque

T = int(input())

for _ in range(T):
    p = sys.stdin.readline().rstrip()
    n = int(input())
    arr = sys.stdin.readline().rstrip()[1:-1].split(",")
    q = deque(arr)

    rev, left, right = 0, 0, len(q) - 1
    error = 0
    if n == 0:
        q = []
        left = 0
        right = 0

    for i in p:
        if i == 'R':
            rev += 1
        elif i == 'D':
            if len(q) < 1:
                error = 1
                print("error")
                break
            else:
                if rev % 2 == 0:
                    q.popleft()
                else:
                    q.pop()

    if error == 0:
        if rev % 2 == 0:
            print("[" + ",".join(q) + "]")
        else:
            q.reverse()
            print("[" + ",".join(q) + "]")
