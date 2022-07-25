from collections import deque


def move(w1, w2, p_board):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    n_o_f = []

    w1x, w1y, w2x, w2y = w1[0], w1[1], w2[0], w2[1]
    for i in range(4):
        nw1 = (w1x + dx[i], w1y + dy[i])
        nw2 = (w2x + dx[i], w2y + dy[i])
        if p_board[nw1[0]][nw1[1]] == 0 and p_board[nw2[0]][nw2[1]] == 0:
            n_o_f.append((nw1, nw2))

    if w1[0] == w2[0]:
        for n in [-1, 1]:
            w1n = w1[0] + n
            w2n = w2[0] + n
            if p_board[w1n][w1[1]] == 0 and p_board[w2n][w2[1]] == 0:
                n_o_f.append((w1, (w1n, w1[1])))
                n_o_f.append((w2, (w2n, w2[1])))
    else:
        for n in [-1, 1]:
            w1n = w1[1] + n
            w2n = w2[1] + n
            if p_board[w1[0]][w1n] == 0 and p_board[w2[0]][w2n] == 0:
                n_o_f.append(((w1[0], w1n), w1))
                n_o_f.append(((w2[0], w2n), w2))
    return n_o_f


def solution(board):
    N = len(board)
    p_board = [[1] * (N + 2) for _ in range(N + 2)]
    for i in range(N):
        for j in range(N):
            p_board[i + 1][j + 1] = board[i][j]

    q = deque()
    q.append(((1, 1), (1, 2), 0))
    visited = [((1, 1), (1, 2))]
    while q:
        w1, w2, cnt = q.popleft()
        if w1 == (N, N) or w2 == (N, N):
            return cnt

        for w1n, w2n in move(w1, w2, p_board):
            if (w1n, w2n) not in visited:
                visited.append((w1n, w2n))
                q.append((w1n, w2n, cnt + 1))
