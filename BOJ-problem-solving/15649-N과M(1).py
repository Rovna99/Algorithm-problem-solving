N, M = map(int, input().split())
num = []
visit = [False] * N


def NaM(result):
    if result == M:
        return print(' '.join(map(str, num)))

    for i in range(len(visit)):
        if not visit[i]:
            visit[i] = True
            num.append(i+1)
            NaM(result+1)
            visit[i] = False
            num.pop()


NaM(0)

