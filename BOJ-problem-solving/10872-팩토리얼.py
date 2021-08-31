# 1
def factorial(n):
    if n <= 1:
        return 1
    if n > 1:
        return n*factorial(n-1)


print(factorial(int(input())))


# 2 (쪼끔 더 빠르다)
def factorial(n, result):
    if n == 1 or n == 0:
        return print(result)
    if n > 1:
        result *= n
        n -= 1
    factorial(n, result)


n = int(input())
factorial(n, 1)