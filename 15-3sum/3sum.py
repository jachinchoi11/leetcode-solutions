class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # for 3 sum essntially we can have a three pointers 
        # this is a trickky proiblem as well 

        # we will have a pointer initiaized that wil start from 0 all the way to the 
        # we can hvea. hashset that compares the three values 

        nums.sort()
        res = []

        for main in range(0, len(nums) - 2):
            if main > 0 and nums[main] == nums[main - 1]:
                continue
            left, right = main + 1, len(nums) - 1
            while left < right:
                currSum = nums[main] + nums[left] + nums[right]
                if currSum > 0:
                    right -= 1
                elif currSum < 0:
                    left += 1
                else:
                    res.append([nums[main], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    left += 1
                    right -= 1
        return res

                    
                    