from collections import deque


def move(w1, w2, wall_board):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    n_o_f = [] #이동할 수 있는 모든 경우의 수를 담는 배열
    #순서대로 첫번째 바퀴의 x,y 좌표와 두번째 바퀴의 x,y 좌표
    w1x, w1y, w2x, w2y = w1[0], w1[1], w2[0], w2[1]
    for i in range(4):
        #각 바퀴에 dx,dy를 더해 상,하,좌,우이동이 가능한지 확인, 가능하다면 배열에 추가한다.
        w1x_n, w1y_n, w2x_n, w2y_n = w1x+dx[i], w1y+dy[i], w2x+dx[i], w2y+dy[i]
        if wall_board[w1x_n][w1y_n] == 0 and wall_board[w2x_n][w2y_n] == 0:
            n_o_f.append({(w1x_n, w1y_n), (w2x_n, w2y_n)})

    if w1x == w2x: # 로봇: ㅡ모양일시 상, 하 회전
        for n in [-1, 1]:
            #현재 바퀴 기준 위쪽, 아래쪽에 벽이 없는지 체크
            if wall_board[w1x + n][w1y] == 0 and wall_board[w2x + n][w2y] == 0:
                #없다면 각각 위, 아래로 회전한 경우를 저장
                n_o_f.append({(w1x, w1y), (w1x + n, w1y)})
                n_o_f.append({(w2x, w2y), (w2x + n, w2y)})
    else: # 로봇: ㅣ모양일시 좌, 우 회전
        for n in [-1, 1]:
            #현재 바퀴 기준 왼쪽, 오른쪽칸에 벽이 없는지 체크
            if wall_board[w1x][w1y + n] == 0 and wall_board[w2x][w2y + n] == 0:
                #없다면 각각 좌, 우 회전한 경우를 저장
                n_o_f.append({(w1x, w1y), (w1x, w1y + n)})
                n_o_f.append({(w2x, w2y), (w2x, w2y + n)})
    return n_o_f


def solution(board):
    N = len(board)
    #상하좌우 한칸씩 벽을 만드는 보드를 새로 생성하고, 외벽안은 기존 보드와 동일하게 가져간다.
    wall_board = [[1]*(N+2) for _ in range(N+2)]
    for i in range(N):
        for j in range(N):
            wall_board[i+1][j+1] = board[i][j]

    q = deque()
    q.append(((1, 1), (1, 2), 0))
    visited = [((1, 1), (1, 2))]
    while q:
        w1, w2, cnt = q.popleft()
        if w1 == (N, N) or w2 == (N, N):
            return cnt

        for w1n, w2n in move(w1, w2, wall_board):  #저장해놓은 다음 위치를 가져온다.
            if (w1n, w2n) not in visited:
                visited.append((w1n, w2n))
                q.append((w1n, w2n, cnt+1))


b =  [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
print(solution(b))

n_o_f = [((1,2),(2,1))]


