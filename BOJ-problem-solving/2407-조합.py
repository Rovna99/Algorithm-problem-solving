n, m = map(int, input().split())

# 공식 문제로 기초적인 공식을 알고 있으면 해결된다.
def factorial(n):
    num = 1
    for i in range(n):
        num *= (i+1)
    return num


N = factorial(n)
M = factorial(n-m)*factorial(m)

print(N//M)
