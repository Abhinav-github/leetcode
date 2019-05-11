#Say you have an array for which the ith element is the price of a given stock on day i.
#If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock),
#design an algorithm to find the maximum profit.
# Note that you cannot sell a stock before you buy one.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = sys.maxsize
        for i in range(len(prices)):
            min_price = min(min_price,prices[i])
            curr_profit = prices[i] - min_price
            max_profit = max(max_profit, curr_profit)
        return max_profit
