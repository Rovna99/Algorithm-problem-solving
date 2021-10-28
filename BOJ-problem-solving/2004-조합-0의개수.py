import sys


def count(n, k):
    cnt = 0
    while n:
        n //= k
        cnt += n
    return cnt


N, K = map(int, sys.stdin.readline().rstrip().split())

five_multi = count(N, 5) - count(K, 5) - count(N - K, 5)
two_multi = count(N, 2) - count(K, 2) - count(N - K, 2)

print(min(five_multi, two_multi))
