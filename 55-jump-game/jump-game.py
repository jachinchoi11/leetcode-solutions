class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # we want to see if we can reach the last index
            # so we can greedily take the farthest roiute no matter what
            # the second we go to an index and our reach of index < curr_index: return Fase
            # otherwise we reutn True

        max_reach = 0

        for index, num in enumerate(nums):

            if index > max_reach:
                return False
            
            max_reach = max(index + num, max_reach)
        
        return True


