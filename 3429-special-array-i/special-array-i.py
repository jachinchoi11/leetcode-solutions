class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        # you can either compare like from 1 index to nums.index - 1
        # but also you can just start from 1 and compare the nex tone im pretty xure
            # that way you have less repeated checks 


        
        for index in range(len(nums) - 1):
            curr_parity = nums[index] % 2
            next_parity = nums[index + 1] % 2
            if next_parity == curr_parity:
                return False
        return True