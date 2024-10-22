class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l, r = 0,0
        maxProfit = 0
        while r < len(prices):
            profit = prices[r] - prices[l]
            while prices[r] < prices[l]:
                l = r
            maxProfit = max(maxProfit, profit)
            r += 1
        
        return maxProfit 