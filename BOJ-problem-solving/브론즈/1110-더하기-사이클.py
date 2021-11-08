import sys

N = int(sys.stdin.readline())
cnt = 0
n = N

while True:
    a = n // 10  # n의 십의 자리 숫자
    b = n % 10  # n의 일의 자리 숫자
    c = (a+b) % 10  # 새 n의 일의 자리 숫자, 합의 오른쪽 숫자이기 때문에, 10으로 나눔
    n = (b*10) + c  # 새로운 n
    cnt += 1  # 사이클 길이
    if n == N:  # 다시 같아진다면, 종료 후 사이클 길이 출력
        break

print(cnt)
