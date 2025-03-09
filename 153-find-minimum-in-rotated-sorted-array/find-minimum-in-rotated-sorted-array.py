class Solution:
    def findMin(self, nums: List[int]) -> int:

        # a binary search of some kind to find the minimum value 
        # we would use two pointers in this case 

        left, right = 0, len(nums) - 1

        while left <= right:
            middle = left + (right - left) // 2
            if nums[middle] < nums[right]:
                # here we know we want to go down, however, that value in the middle might be the value we need
                right = middle
            else:
                # because we can rule it out bc the middle is bigger than right - meaning it can't be min
                left = middle + 1
        return nums[middle] # because we have to return a converged value, we have to use <= 


        # 3,4,5,1,2

        # left = 0, right = 4

        # left = 3 right = 3

