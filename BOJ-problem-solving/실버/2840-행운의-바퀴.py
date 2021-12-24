N, K = map(int, input().split())
w = ['?' for _ in range(N)]
for i in range(K):
    spin = input().split()
    s = int(spin[0]) % N
    s_char = str(spin[1])

    w = w[-s:] + w[:-s]
    if w[0] == '?':
        if s_char in w:
            print('!')
            break
        w[0] = s_char
    elif w[0] == s_char:
        continue
    else:
        print('!')
        break
else:
    print(''.join(w))
