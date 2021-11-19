N = int(input())
b = [list(map(int, input())) for _ in range(N)]


def cut(x, y, N):
    if N == 1:
        return str(b[x][y])
    bw = b[x][y]
    result = []

    for i in range(x, x+N):
        for j in range(y, y+N):
            if bw != b[i][j]:
                result.append('(')
                result.extend(cut(x, y, N//2))
                result.extend(cut(x, y+N//2, N//2))
                result.extend(cut(x+N//2, y, N//2))
                result.extend(cut(x+N//2, y+N//2, N//2))
                result.append(')')
                return result

    return str(b[x][y])


print(''.join(cut(0, 0, N)))

