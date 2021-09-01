import sys

data = [True for x in range(10001)]
data[0], data[1] = False, False
# 에라토스테네스의 체로 소수 구별.10000**0.5=100, 값이 1이면 소수
for i in range(2, 100):
    for j in range(i*2, 10001, i):
        data[j] = False


#중앙값에 근접할수록 차가 적다. 중앙값부터 계산한다.
for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    for num in range(n//2, n):
            if data[num]:
                if data[n - num]:
                    print(n - num, num, sep=' ')
                    break
