class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1
        
        while l <= r:
            m = (l + r) // 2
            value = nums[m]
            if value > target:
                r = m - 1
            elif value < target:
                l = m + 1
            else:
                return m
        return -1 