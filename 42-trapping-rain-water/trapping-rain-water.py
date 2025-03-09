class Solution:
    def trap(self, height: List[int]) -> int:

        # first brute force approach is, teh way that how much water can be in your specific squre 
        # is dependent on the max height on both sides (the minimum of the max ehught) - your height

        # so maybe create a left_max array and a right_max array (precompute this)
            # iterate over and find out how mcuh water is in each one 
        
        
        left_max = [0] * len(height)
        right_max = [0] * len(height)
        res = 0

        curr_left_max = 0

        for index in range(len(height)):
            left_max[index] = curr_left_max
            curr_left_max = max(curr_left_max, height[index])
        
        curr_right_max = 0

        for index in range(len(height) - 1, -1 , -1):
            right_max[index] = curr_right_max
            curr_right_max = max(curr_right_max, height[index])
        print(right_max, left_max)
        for index in range(len(height)):
            right_m = right_max[index]
            left_m = left_max[index]

            minimum_height = min(left_m, right_m)
            if minimum_height < height[index]:
                continue
            res += (minimum_height - height[index])
        
        return res

        



