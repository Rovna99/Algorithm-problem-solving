import sys

T = int(sys.stdin.readline())
for i in range(T):
    N, M = map(int, sys.stdin.readline().split())
    num = list(map(int, sys.stdin.readline().split()))
    num2 = [0 for i in range(N)]
    num2[M] = 1
    cnt = 0
    while True:
        if num[0] == max(num):
            cnt += 1
            if num2[0] == 1:
                print(cnt)
                break
            else:
                del num[0]
                del num2[0]
        else:
            num.append(num[0])
            del num[0]
            num2.append(num2[0])
            del num2[0]


