class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # initial answer for me would be to just go and get the total mutliplicative product
        # and then go to each one and dividde the current number
            # you can not use the division poperator

        # so an observation of that is literally just the definiton 
            # you have a left and a right operator 
            # and you want to multiply everythign on your lieft * everything on your right
        
        # so maybe we make a left_product array and a right_product array
        # precompute those values, and then just multiply it at the very end 
            # three pass solutin
                # O(n) time and O(n) space
        


        ans = [1] * len(nums)

        for index in range(1, len(nums)):
            ans[index] = ans[index - 1] * nums[index - 1]
        right_running_product = 1

        for index in range(len(nums) - 2, -1, -1):
            right_running_product *= nums[index + 1]
            ans[index] = right_running_product * ans[index]
        return ans
        



        


        

        
