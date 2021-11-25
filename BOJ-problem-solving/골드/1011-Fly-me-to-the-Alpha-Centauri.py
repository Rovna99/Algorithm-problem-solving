T = int(input())

for i in range(T):
    x, y = map(int, input().split())
    dis = y - x
    cnt = 0
    move = 1
    move_p = 0

    while move_p < dis:
        cnt += 1
        move_p += move
        if not cnt % 2:
            move += 1
    print(cnt)
