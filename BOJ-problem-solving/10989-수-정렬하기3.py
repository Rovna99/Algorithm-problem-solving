import sys
#메모리 제한이 있따..그래서 무조건 배열 하나로 계수 정렬을 통해 정렬해야 한다..!

num = [0] * 10001
for _ in range(int(sys.stdin.readline())):
    num[int(sys.stdin.readline())] += 1

for i in range(len(num)):
    if num[i] != 0:
        for _ in range(num[i]):
            print(i)
