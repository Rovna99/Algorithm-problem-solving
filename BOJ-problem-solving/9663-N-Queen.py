n, result = int(input()), 0
a, b, c = [False]*n, [False]*(2*n-1), [False]*(2*n-1)


def solution(i):
    global result
    if i == n:
        result += 1
        return
    for j in range(n):
        if not (a[j] or b[i+j] or c[i-j+n-1]):
            a[j] = b[i+j] = c[i-j+n-1] = True
            solution(i+1)
            a[j] = b[i+j] = c[i-j+n-1] = False


solution(0)
print(result)




