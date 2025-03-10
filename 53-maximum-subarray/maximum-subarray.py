class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # i was thinking initially we could try to do a sliding window --> however, cause of negative numebrs
        # this won't work for our sliding window mechanic

        # i thikn the play here is to always take the higher numbers --> be greedy about it
            # we will have a running sum to keep track of whatever subarray we're working with
                # onlu take positive sums --> otherwise go to 0 
        
        max_sum = nums[0]
        curr_sum = 0
        for num in nums:
            curr_sum = max(curr_sum + num, num)
            max_sum = max(max_sum, curr_sum)
        return max_sum



