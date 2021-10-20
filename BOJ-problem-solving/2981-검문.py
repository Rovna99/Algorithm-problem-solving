def gcd(x, y):
    while x % y != 0:
        x, y = y, x % y
    return y


N = int(input())
M = [int(input()) for _ in range(N)]
M.sort()

answer = M[1] - M[0]
for i in range(2, len(M)):
    answer = gcd(answer, M[i] - M[i-1])

result = [answer]

for i in range(2, int(answer**0.5)+1):
    if answer % i == 0:
        print(i, end=' ')
        if i != answer//i:
            result.insert(0, answer//i)

for num in result:
    print(num, end=' ')