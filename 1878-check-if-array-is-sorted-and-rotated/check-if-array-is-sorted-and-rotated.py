class Solution:
    def check(self, nums: List[int]) -> bool:
        decreasingFlag = False
        decreasingNumber = float('inf')
        for index in range(len(nums) - 1):
            if nums[index] > nums[index + 1]:
                if decreasingFlag:
                    return False
                else:
                    decreasingFlag = True
                    decreasingNumber = nums[index]
            elif nums[index + 1] > decreasingNumber or nums[index] > decreasingNumber:
                return False

        if nums[len(nums) - 1] > nums[0]:
            if decreasingFlag:
                return False
        return True