price = []
#1 그리디 알고리즘
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        for i in range(len(prices) - 1):
            if price[i+1] > price[i]:
                result += price[i+1]-price[i]
        return result

#2 파이썬다운 방식
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(max(prices[i+1] - prices[i], 0) for i in range(len(prices) - 1))