class Solution:
    import math
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        minRate = 1 
        maxRate = max(piles)


        while minRate < maxRate:
            
            middleRate = (minRate + maxRate) // 2
            hours = self.calculateHours(middleRate, piles)

            if hours <= h:
                maxRate = middleRate
            else:
                minRate =  middleRate + 1
        return minRate

        

    def calculateHours(self, middleRate, piles):
        res = 0
        # keeps track of how many hours 
        for num in piles:
            res += ceil(num/middleRate)
        return res 

                
