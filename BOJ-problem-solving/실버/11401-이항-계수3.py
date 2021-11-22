N, K = map(int, input().split())
div = 1000000007


def fact(num, mod):
    result = 1
    for i in range(1, num + 1):
        result = result * i % mod
    return result


def power(num, p, mod):
    if p == 1:
        return num % mod
    temp = power(num, p//2, mod)

    if p % 2 == 0:
        return temp * temp % mod
    else:
        return temp * temp * num % mod


a = fact(N, div)
b = power((fact(N-K, div)*fact(K, div)), div-2, div)
print(a * b % div)

# N, K = map(int, input().split())
# div = 1000000007
#
# a, b = 1, 1
# for i in range(1, N+1):
#     a = (a * i) % div
# for i in range(1, N-K+1):
#     b = (b * i) % div
# for i in range(1, K+1):
#     b = (b * i) % div
#
#
# def power(num, p, mod):
#     if p == 1:
#         return num % mod
#     temp = power(num, p//2, mod)
#
#     if p % 2 == 0:
#         return temp * temp % mod
#     else:
#         return temp * temp * num % mod
#
#
# b = power(b, div - 2, div)
# print(a * b % div)


