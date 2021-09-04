import collections
#1 메모이제이션
class Solution:
    dp = collections.defaultdict(int)

    def fib(self, N: int) -> int:
        if N <= 1:
            return N

        if self.dp[N]:
            return self.dp[N]

        self.dp[N] = self.fib(N - 1) + self.fib(N - 2)
        return self.dp[N]
#2 타뷸레이션
class Solution:
    dp = collections.defaultdict(int)

    def fib(self, N: int) -> int:
        self.dp[1] = 1

        for i in range(2, N + 1):
            self.dp[i] = self.dp[i - 1] + self.dp[i - 2]
        return self.dp[N]

#3 두 변수만 이용(공간 절약)
class Solution:
    def fib(self, N: int) -> int:
        x, y = 0, 1
        for i in range(0, N):
            x, y = y, x + y
        return x