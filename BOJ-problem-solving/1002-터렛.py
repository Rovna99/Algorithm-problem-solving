from math import sqrt
T = int(input())
for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dis = sqrt((x2 - x1)**2 + (y2 - y1)**2)
    if dis == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        if dis > r1+r2 or r2 > r1+dis or r1 > r2+dis:
            print(0)
        elif abs(r1 - r2) == dis or r1 + r2 == dis:
            print(1)
        else:
            print(2)





