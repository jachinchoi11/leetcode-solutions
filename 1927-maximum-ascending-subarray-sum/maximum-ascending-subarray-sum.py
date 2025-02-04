class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maxSum = 0 
        currSum = nums[0]

        for r in range(1, len(nums)):
            if nums[r] <= nums[r - 1]:
                maxSum = max(currSum, maxSum)
                currSum = nums[r]
            else:
                currSum += nums[r]
            print(currSum)
        return max(maxSum, currSum)
                        
                