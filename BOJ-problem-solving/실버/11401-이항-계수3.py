def DCA(a, b):
    if b == 0:
        return 1
    if b % 2:
        return (DCA(a, b//2) ** 2 * a) % div
    else:
        return (DCA(a, b//2) ** 2) % div


N, K = map(int, input().split())
div = 1000000007

fact = [1 for i in range(N+1)]

for i in range(2, N+1):
    fact[i] = fact[i-1] * i % div

n = fact[N]
k = (fact[N-K] * fact[K]) % div

print((n % div) * (DCA(k, div-2) % div) % div)


