def g_gcd(x, y):
    while x % y != 0:
        x, y = y, x % y
    return y


N = int(input())
circle = list(map(int, input().split()))
st = circle[0]
result = []

for i in range(1, len(circle)):
    gcd = g_gcd(st, circle[i])
    a = st // gcd
    b = circle[i] // gcd
    result.append([a, b])

for a, b in result:
    print('{}/{}'.format(a, b))
