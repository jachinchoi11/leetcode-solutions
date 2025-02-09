import math
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        
        # oh this is a very simple problem, we should essentially go about it as we go through the list
        # we can use a hashmap in this case
            # have to think about we are going to use this hashmap, but the idea is that we will add in values as we go 
            # that's waht i was thinkking for real, so myabe lets think about the good paris and do total pairs - good pairs = bad paris 

            # so. a good pair woul dbe that j - i == nums[j] - nums[i]
        
        # total pairs = math.factorial(len(nums))

        # essentially, we need to remanipualte this equation to go j - nums[j]. == i - nums[i]

        # basically we find if this is even possible, and we have a counter for this reason, we would add (index - value ) += 1 in our defaultdict
        # then any time we encounter it, we would actually add it to the amount of good pairs that we have 
        # then we could subtract the total pairs of this value 

        total_pairs = 0

        for i in range(1, len(nums)):
            total_pairs += i
        
        index_value_map = defaultdict(int)
        good_pairs = 0

        for index, num in enumerate(nums):
            curr = index - num
            if curr in index_value_map:
                good_pairs += index_value_map[curr]
            index_value_map[curr] += 1        
        
        return total_pairs - good_pairs
