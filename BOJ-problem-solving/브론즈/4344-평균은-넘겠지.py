import sys

N = int(input())

for _ in range(N):
    s = list(map(int, sys.stdin.readline().rstrip().split()))  # 입력값 리스트로 받기
    aver = (sum(s) - s[0]) // s[0]  # 평균 구하기
    cnt = 0

    for i in range(1, len(s)):  # 첫번째를 제외한 나머지 중
        if s[i] > aver:  # 평균을 넘으면
            cnt += 1  # 넘는 학생 수 체크
    print("{:.3f}%".format(100/s[0]*cnt))  # 결과값 출력
