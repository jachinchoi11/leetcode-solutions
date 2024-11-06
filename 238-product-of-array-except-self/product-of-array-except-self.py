class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)
        res = []
        for index in range(1, len(nums)):
            currNum = nums[index - 1] * prefix[index - 1]
            prefix[index] = currNum
        
        for index in range(len(nums) -2, -1,-1):
            currNum = nums[index + 1] * postfix[index + 1]
            postfix[index] = currNum
        
        for index in range(len(nums)):
            res.append(postfix[index] * prefix[index])
        
        return res

        
        
