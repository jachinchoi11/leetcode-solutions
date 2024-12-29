class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0

        for right in range(len(nums)):
            # we will keep on going whiel we see a regular number that is not in the hashset, but as soon as we do see one 
            # we can iterate right until we see a non one and set left iterate right
            if nums[left] == nums[right]:
                continue
            else:
                left += 1
                nums[left], nums[right] = nums[right], nums[left]
        
        return left + 1
