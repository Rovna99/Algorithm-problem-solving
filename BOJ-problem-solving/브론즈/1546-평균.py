import sys

N = int(sys.stdin.readline())
score = list(map(int, sys.stdin.readline().split()))  # 점수값을 한번에 리스트로 입력받음
max_s = max(score)  # 현재 최고 점수
aver = 0  # 평균값을 0으로 초기화
for i in range(N):
    score[i] = score[i] / max_s * 100  # i번째 점수를 새로운 값으로 변경
    aver += score[i]  # 새로운 점수를 평균값에 더해준다

aver /= N  # 입력받은 성적 수로 평균값을 구한다.

print(aver)
