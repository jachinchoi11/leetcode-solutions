class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0

        for index in range(len(nums)):
            if nums[index] != 0:
                nums[left], nums[index] = nums[index] , nums[left]
                left += 1
    
