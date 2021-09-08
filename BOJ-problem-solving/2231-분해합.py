N = int(input())
m = len(str(N))


def result(n):
    if n > 0:
        o_n = str(n)
        for num in o_n:
            n += int(num)
        return n


for i in range(N-(m*9), N+1):
    if result(i) == N:
        print(i)
        break
    elif i == N:
        print(0)
