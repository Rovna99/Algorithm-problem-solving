N, M, R = map(int, input().split())
rotate_list = [list(map(int, input().split())) for _ in range(N)]

for _ in range(R):
    for i in range(min(N, M) // 2):
        f_x, f_y = i, i
        f_value = rotate_list[f_x][f_y]

        for j in range(i+1, N-i):
            f_x = j
            prev = rotate_list[f_x][f_y]
            rotate_list[f_x][f_y] = f_value
            f_value = prev

        for j in range(i+1, M-i):
            f_y = j
            prev = rotate_list[f_x][f_y]
            rotate_list[f_x][f_y] = f_value
            f_value = prev

        for j in range(i+1, N-i):
            f_x = N - j - 1
            prev = rotate_list[f_x][f_y]
            rotate_list[f_x][f_y] = f_value
            f_value = prev

        for j in range(i+1, M-i):
            f_y = M - j - 1
            prev = rotate_list[f_x][f_y]
            rotate_list[f_x][f_y] = f_value
            f_value = prev

for i in range(N):
    for j in range(M):
        print(rotate_list[i][j], end=' ')
    print()
