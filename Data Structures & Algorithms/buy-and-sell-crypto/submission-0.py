class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        cost = prices[0]
        for i in range(1,len(prices)):
            max_profit = max(max_profit,prices[i]-cost)
            cost = min(cost,prices[i])
        return max_profit
        