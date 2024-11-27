class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        # make a prefix sum of the max subarray as you go check if the k - currSum is in there 
        # you would solve the current array length 
        # then you would have to check if the target number - currSum is in the prefixSum
        # calculate the index and then maximize the width of it 

        prefixSum = {0:0}
        currSum = 0
        maxSubArray = False

        for index, num in enumerate(nums, start = 1):
            currSum += nums[index - 1]
            targetNum = currSum - k
            if targetNum in prefixSum:
                prevIndex = prefixSum[targetNum]
                maxSubArray = max(index - prevIndex, maxSubArray)
            
            if currSum not in prefixSum:
                prefixSum[currSum] = index
        
        return maxSubArray if maxSubArray != False else 0