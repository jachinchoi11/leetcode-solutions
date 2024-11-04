class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currSum = sum(nums[:k])
        maxSum = currSum
        l = 0
        for r in range(k, len(nums)):
            currSum -= nums[l]
            l += 1
            currSum += nums[r]
            maxSum = max(maxSum, currSum)

        return maxSum / k