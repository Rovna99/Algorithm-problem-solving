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

#파이썬으로도 시간초과 안되는 코드

def dfs(depth):
    if depth == blank_num:
        for v in board:
            print(' '.join(map(str, v)))
        exit(0)
    y,x=pos[depth]
    for n in range(1,10):
        if not row_arr[y][n] and not col_arr[x][n] and not box_arr[y//3*3+x//3][n]:
            row_arr[y][n] = col_arr[x][n] = box_arr[y//3*3+x//3][n] = True
            board[y][x]=n
            dfs(depth+1)
            row_arr[y][n] = col_arr[x][n] = box_arr[y//3*3+x//3][n] = False
            board[y][x]=0

board=[list(map(int, input().split())) for _ in range(9)]
row_arr=[[False]*10 for _ in range(10)]
col_arr=[[False]*10 for _ in range(10)]
box_arr=[[False]*10 for _ in range(10)]

pos=[]
for r in range(9):
    for c in range(9):
        if not board[r][c]: pos.append([r,c])
        else:
            row_arr[r][board[r][c]]=True
            col_arr[c][board[r][c]]=True
            box_arr[r//3*3+c//3][board[r][c]]=True

blank_num=len(pos)
dfs(0)