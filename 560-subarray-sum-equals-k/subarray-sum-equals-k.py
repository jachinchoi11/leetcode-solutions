class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        # initially, i was thikning of usign sldiign windows --> this woudl be possible with all positive numbers
        # however, there are negative numbers, meaning we would not know what could cause the mechanci to adjust the window

        # maybe we can create a prefix sums for the arrays 
            # we can see if we ever do get to k
                # but also we can check if we ever saw the curr_sum - k 
                
                # if we did that search in an array
                    # that woudl lead to greater coplexity potentialyl up to O(size - 1)

                # so we have to create a frequency table --> for how many tiems we saw this
                    # was thinking set intiialy, but what we ahve several instacnes of a sum
        # we will have a basic variabel for current_sum
            # and then put that in a hashmap 
        
        res = 0
        curr_sum = 0
        sum_tracker = {0: 1}

        for num in nums:
            curr_sum += num
            if curr_sum - k in sum_tracker:
                res += sum_tracker[curr_sum - k]
                
            if curr_sum in sum_tracker:
                sum_tracker[curr_sum] += 1
            else:
                sum_tracker[curr_sum] = 1

        return res




