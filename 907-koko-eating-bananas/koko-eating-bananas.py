import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # we want to find the minimum rate of time it wil take to finish in h hours
        # so initally, im thinkign waht if we just start 1 to the max --> and try and see if that will work
            # the first time it will work 
        

        # so i'm thinking we can potentially speed up this process as well, max time --> the max amount in a pile
            # im thiking we can do a binary search of some sort that biases minimum values
            # we can have a helper funciton whether it is possible in h hours, and always try to shrink if possible 

        max_value = max(piles) # O(n) operation, where we look for max in piles
        min_value = 1
        ans = float('inf')

        while min_value <= max_value:
            middle_rate = min_value + (max_value - min_value) // 2
            eligible = self.is_valid(piles, middle_rate, h)
            if eligible:
                ans = min(ans, middle_rate)
                max_value = middle_rate - 1
            else:
                min_value = middle_rate + 1
        return ans 
    
    def is_valid(self, piles, rate, h):
        time = 0
        for pile in piles:
            time += math.ceil(pile/rate)
        return time <= h
        
        
        



        
