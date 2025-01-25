class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        # interesting so we want to use prefix sums
        # to count how many odd numbers there are in the nums
        # and if we've ever seen x - k odd numbers, then we would add that in 

        count = {0:1}
        curr_odd_count = 0
        res = 0 

        
        for num in nums:
            if num % 2 == 1:
                curr_odd_count += 1
            if curr_odd_count - k in count:
                res += count[curr_odd_count -k]
            if curr_odd_count in count:
                count[curr_odd_count] += 1
            else:
                count[curr_odd_count] = 1
        return res
            
         