n = int(input())
cnt = 0
for _ in range(n):
    s = input()
    a = [s[0]]
    e = False
    for i in range(1, len(s)):
            if s[i] != a[-1]:
                if s[i] in a:
                    e = True
                    break
                else:
                    a.append(s[i])
    if not e:
        cnt += 1
print(cnt)

