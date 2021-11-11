N, M = map(int, input().split())

num = list(map(int, input().split()))
q = [_ for _ in range(1, N+1)]
cnt = 0
for i in range(M):
    len_q = len(q)
    idx_q = q.index(num[i])

    if idx_q < len_q - idx_q:
        while True:
            if q[0] == num[i]:
                del q[0]
                break
            else:
                q.append(q[0])
                del q[0]
                cnt += 1
    else:
        while True:
            if q[0] == num[i]:
                del q[0]
                break
            else:
                q.insert(0, q[-1])
                del q[-1]
                cnt += 1

print(cnt)
