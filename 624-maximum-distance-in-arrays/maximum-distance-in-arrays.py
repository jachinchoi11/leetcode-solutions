class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        
        # ok so we can actually iterate through this one at a time 
        # we have to take advantage of the fact that its sorted and we can solve through this in a single pass

        result = 0 
        ultMin = arrays[0][0]
        ultMax = arrays[0][-1]

        for index in range(1, len(arrays)):
            array = arrays[index]
            currResult = max(ultMax - array[0], array[-1] - ultMin)
            ultMin = min(array[0], ultMin)
            ultMax = max(array[-1], ultMax)
            result = max(currResult, result)
        
        return result
