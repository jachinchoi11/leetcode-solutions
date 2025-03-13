class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        

        # so we can just check for the largest integer that comes out once 

        count_map = Counter(nums)
        res = -1

        for num, freq in count_map.items():
            if freq == 1:
                res = max(res, num)
        
        return res 

