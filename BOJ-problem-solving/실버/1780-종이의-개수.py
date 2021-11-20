import sys

input = sys.stdin.readline
N = int(input())
p = [list(map(int, input().strip().split())) for _ in range(N)]
result = {  # 각 숫자의 개수를 세기 위해 dict을 사용
    -1: 0,
    0: 0,
    1: 0
}


def cut(x, y, n):
    num = p[x][y]  # 현재 숫자
    if n == 1:
        result[num] += 1  # 1개라면, 현 숫자의 개수를 +1
        return
    for i in range(x, x+n):  # 첫번째부터 끝까지
        for j in range(y, y+n):
            if p[i][j] != num:  # 만약 첫번째숫자와 다른숫자가 나온다면
                # 9등분 한다 했으므로 N을 3으로 나눈후,
                # 한번 더한 것, 두번 더한걸로 위치를 cut 함수에 넣어준다
                cut(x, y, n // 3)
                cut(x, y + n // 3, n // 3)
                cut(x, y + n // 3 * 2, n // 3)
                cut(x + n // 3, y, n // 3)
                cut(x + n // 3, y + n // 3, n // 3)
                cut(x + n // 3, y + n // 3 * 2, n // 3)
                cut(x + n // 3 * 2, y, n // 3)
                cut(x + n // 3 * 2, y + n // 3, n // 3)
                cut(x + n // 3 * 2, y + n // 3 * 2, n // 3)
                return

    result[num] += 1  # 첫위치와 숫자가 모두 같다면, 현재 숫자에 +1을 해준다


cut(0, 0, N)
for a in result.values():  # dict의 값을 출력
    print(a)
