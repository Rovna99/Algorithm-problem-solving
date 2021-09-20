N, M = map(int, input().split())
result = []


def NaM(s):
    if len(result) == M:
        print(' '.join(map(str, result)))
        return

    for i in range(s, N+1):
        if i not in result:
            result.append(i)
            NaM(i+1)
            result.pop()


NaM(1)


