class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        # you can flip at most k 0s

        # so basically our sliding window for tis approach as we ceck and see how many 1s there are
        # when we see a 0, we can get zero_count 
        # and then our while statement that cheks for the a valid sliding window will be 
            # (right - left + 1) - zero_count > k
            # then we have to keep on shaving until the zero_count goes down
        # then we can update our res 

        left, right, res, zero_count = 0, 0, 0, 0

        while right < len(nums):

            curr_number = nums[right]
            if curr_number == 0:
                zero_count += 1
    
            while zero_count > k:
                left_number = nums[left]
                if left_number == 0:
                    zero_count -= 1
                left += 1
            res = max(res, (right - left + 1))
            right += 1
        return res
