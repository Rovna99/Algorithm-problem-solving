import collections

s = 1
v = 2
e = 3
result = []


def hanoi(n, start, end, sev):
    result.append(start)
    if n == 1:
        return print(start, end, sep=' ')
    hanoi(n - 1, start, sev, end)
    print(start, end, sep=' ')
    hanoi(n - 1, sev, end, start)


n = int(input())
print(2**n - 1)
hanoi(n, s, e, v)
