class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # so essentially we want to get the maximum profit from this list 
            # we can buy one time and sell it another time 
        
        # if we see a minimum number, we want to shift l += 1, where that is not the case

        
        min_price = float('inf')
        max_profit = 0

        for index in range(len(prices)):
            min_price = min(min_price, prices[index])
            max_profit = max(max_profit, prices[index] - min_price)
        
        
        return max_profit
            
