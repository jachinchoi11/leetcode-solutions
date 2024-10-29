class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # we can take a greedy approach, where we simply just loook for greater elements 
        # we can keep track of a prefix sum where if it is < 0, = 0
        # however, we need to start off sum with first value 

        r = 0
        maxSum = nums[0]
        prefixSum = 0
        
        while r  < len(nums):
            prefixSum += nums[r]
            if nums[r] > maxSum:
                maxSum = nums[r]
            if prefixSum < 0:
                prefixSum = 0
            else:
                maxSum = max(prefixSum, maxSum)
            r += 1
        return maxSum
        
