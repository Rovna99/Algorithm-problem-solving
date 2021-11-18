n = input()
while n != '0':  # 0을 입력 받으면 종료

    if n == n[::-1]:  # n이 처음부터 끝까지 -1칸 간격으로 비교
        print('yes')
    else:
        print('no')

    n = input()
