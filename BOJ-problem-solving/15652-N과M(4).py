N, M = map(int, input().split())
result = []


def NaM(s):
    if len(result) == M:
        print(' '.join(map(str, result)))
        return

    for i in range(1, N+1):
        if len(result) > 0 and result[0] > i:
            continue
        else:
            result.append(i)
            NaM(i + 1)
            result.pop()


NaM(1)
