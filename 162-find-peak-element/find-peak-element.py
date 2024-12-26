class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # it needs to be logn, but the arr is not sorted 
        # find a trick to use to find whether or not it will work

        # the only thing that I know that is binary search, so find a way to mkae this work
        def isValid(nums, middle):
            if middle == 0 or nums[middle - 1] < nums[middle]:
                print("hello")
                print(middle)
                if middle == len(nums) - 1 or nums[middle + 1] < nums[middle]:
                    return True
            return False
        
        l, r = 0, len(nums) - 1

        while l <= r:
            middle = (l + r) // 2
            print(l, r)
            if isValid(nums, middle):
                return middle
            else:
                print("a")
                if middle - 1 >= 0 and nums[middle - 1] > nums[middle]:
                    r = middle - 1
                else:
                    l = middle + 1
        return

        # 1,2,3,1
        # 2

        
