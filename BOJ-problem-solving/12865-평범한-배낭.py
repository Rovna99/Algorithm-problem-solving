N, K = map(int, input().split())
bag = [[0, 0]]
pack = [[0 for _ in range(K+1)] for _ in range(N+1)]

for _ in range(N):
    bag.append(list(map(int, input().split())))

for i in range(1, N+1):
    for j in range(1, K+1):
        weight = bag[i][0]
        value = bag[i][1]

        if j < weight:
            pack[i][j] = pack[i-1][j]
        else:
            pack[i][j] = \
                max(value + pack[i-1][j-weight], pack[i-1][j])

print(pack[-1][-1])
