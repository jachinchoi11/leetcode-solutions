class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        # the minimum number of operations to get from startValue to target
        # we want to go from start to end value 
        # what about we find a way to start from the target number and divide by 2 or up it by 1 

        # this was great intiution, and i think this would be potentially easier to think about because we would have more of let's say a base case 
        # in that we always have to add 1 if it is odd, because we don't want to mess with numbers
        # now when it is even, we have to decipher whether or not it woudl be easier to, 
        # essentially, we would always want to divide if when we divide it is higher or equal to the number
        # until we get to a number that is equal to or higher
        # we have two choices from the target value 
            # 1. + 1
            # 2. / 2
        count = 0 
        if target < startValue:
            return startValue - target
        
        while target != startValue:
            if target % 2 != 0:
                target += 1
            else:
                # if the target number is now even, we can make our deicions
                # we want to precompute here what it would look like if we did do the / 2 reduction
                precompute = target // 2
                if target >= startValue:
                    target *= (1/2)
                else:
                    target += 1
            count += 1
        return count
        

        