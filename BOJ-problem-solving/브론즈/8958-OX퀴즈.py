import sys

T = int(input())

for _ in range(T):
    s = sys.stdin.readline().rstrip()  # 한줄 그대로 입력받기
    score = 0  # 점수
    streak = 0  # 연속으로 나온 횟수
    for ox in s:  # 입력받은 s를 하나씩 확인.
        if ox == 'O':  # O 이라면, 연속 횟수에 1을 더해주고 그 점수를 score에 더한다
            streak += 1
            score += streak
        elif ox == 'X':  # X라면, 연속 횟수를 0으로 초기화 해준다.
            streak = 0
    print(score)
