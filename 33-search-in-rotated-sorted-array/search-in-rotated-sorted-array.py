class Solution:
    def search(self, nums: List[int], target: int) -> int:

        pivotIndex = self.findPivot(nums)

        leftSearch = self.binarySearch(nums, 0, pivotIndex - 1, target)

        if leftSearch != -1:
            return leftSearch
        
        return self.binarySearch(nums, pivotIndex, len(nums) - 1, target)


    def binarySearch(self, nums, left, right, target):
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] > target:
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1
            else:
                return middle
        return -1      


    def findPivot(self, nums): 
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[r] > nums[m]:
                r = m
            else:
                l = m + 1
        return m
