import sys

input = sys.stdin.readline
board = [list(map(int, input().split())) for _ in range(9)]
zero = [(x, y) for x in range(9) for y in range(9) if board[x][y] == 0]


def check(x, y):
    nums = [1,2,3,4,5,6,7,8,9]

    for k in range(9):
        if board[x][k] in nums:
            nums.remove(board[x][k])
        if board[k][y] in nums:
            nums.remove(board[k][y])

    x //= 3
    y //= 3

    for i in range(x*3, (x+1)*3):
        for j in range(y*3, (y+1)*3):
            if board[i][j] in nums:
                nums.remove(board[i][j])
    return nums


flag = False


def dfs(x):
    global flag

    if flag:
        return

    if x == len(zero):
        for row in board:
            print(*row)
        flag = True
        return

    else:
        (i, j) = zero[x]
        nums = check(i, j)

        for num in nums:
            board[i][j] = num
            dfs(x + 1)
            board[i][j] = 0


dfs(0)
