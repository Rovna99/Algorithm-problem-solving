while True:
    T, *h = list(map(int, input().split()))
    if T == 0:
        break

    h.insert(0, 0)
    h += [0]
    check = [0]
    area = 0

    for i in range(1, T + 2):
        while check and (h[check[-1]] > h[i]):
            cur_h = check.pop()
            area = max(area, (i - 1 - check[-1])*h[cur_h])
        check.append(i)
    print(area)
