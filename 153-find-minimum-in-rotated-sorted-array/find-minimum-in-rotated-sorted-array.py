class Solution:
    def findMin(self, nums: List[int]) -> int:

        left, right = 0, len(nums) - 1

        while left <= right:
            middle = (left + right) // 2
            if nums[right] > nums[middle]:
                right = middle
            else:
                left = middle + 1
        return nums[middle]
    


