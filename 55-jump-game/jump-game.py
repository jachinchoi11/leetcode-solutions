class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        maxJump = 0
        
        for index in range(len(nums) - 1):
            if maxJump < index:
                return False
            maxJump = max(index + nums[index], maxJump)
        
        if maxJump >= len(nums) - 1:
            return True
        return False
        
                