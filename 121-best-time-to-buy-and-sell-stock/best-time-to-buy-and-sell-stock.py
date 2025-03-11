class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # so essentially we want to get the maximum profit from this list 
            # we can buy one time and sell it another time 
        
        # if we see a minimum number, we want to shift l += 1, where that is not the case

        
        left, right = 0, 0
        max_profit = 0

        while right < len(prices):
            
            curr_profit = prices[right] - prices[left]
            while prices[right] < prices[left]:
                left += 1
                curr_profit = prices[right] - prices[left]
            max_profit = max(curr_profit, max_profit)
            right += 1
        
        return max_profit
            
