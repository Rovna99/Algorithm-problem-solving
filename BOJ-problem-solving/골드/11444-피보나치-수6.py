n = int(input())
mod = 1000000007


def solve(a, num):
    if num == 1:
        return a
    elif num % 2:
        return mul(solve(a, num-1), a)
    else:
        return solve(mul(a, a), num//2)


def mul(a, b):
    temp = [[0]*len(b[0]) for _ in range(2)]
    for i in range(2):
        for j in range(len(b[0])):
            for k in range(2):
                temp[i][j] += a[i][k]*b[k][j]
            temp[i][j] %= mod
    return temp


a = [[1, 1], [1, 0]]
start = [[1], [1]]

if n < 3:
    print(1)
else:
    print(mul(solve(a, n-2), start)[0][0])


