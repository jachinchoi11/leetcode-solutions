class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        sumOfNums = sum(nums)
        currSum = 0

        for index, num in enumerate(nums):
            sumOfNums -= num
            if currSum == sumOfNums:
                return index
            currSum += num
        return -1