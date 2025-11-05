class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = max(prices)
        maximum = 0
        for price in prices:
            if price < minimum:
                minimum = price
            profit = price - minimum
            if profit>maximum:
                maximum = profit
        return maximum

