import sys

N, M = map(int, input().split())
board = []
result = sys.maxsize #답이 최솟값이기에 비교값은 가장 큰 사이즈로
for _ in range(N):
    board.append(input())

for i in range(len(board) - 7):
    for j in range(len(board[i]) - 7):
        w_st = 0 # w로 시작할때 칠해야 될 수
        b_st = 0 # b로 시작할때 칠해야 될 수

        for n in range(i, i+8):
            for m in range(j, j+8):
                if (n+m) % 2 == 0:
                    if board[n][m] != 'W':
                        w_st += 1
                    else:
                        b_st += 1
                else:
                    if board[n][m] != 'B':
                        w_st += 1
                    else:
                        b_st += 1
        result = min(result, b_st, w_st)
print(result)
