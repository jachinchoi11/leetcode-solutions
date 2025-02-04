class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        l = 0
        maxSum = 0 
        currSum = nums[0]

        for r in range(1, len(nums)):
            if nums[r] <= nums[l]:
                maxSum = max(currSum, maxSum)
                currSum = nums[r]
                l = r - 1
            else:
                currSum += nums[r]
            l += 1
            print(currSum)
        return max(maxSum, currSum)
                        
                