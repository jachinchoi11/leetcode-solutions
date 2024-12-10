class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        for index in range(len(nums)):
            if nums[index] < 0:
                result[index] = nums[(index - abs(nums[index])) % len(nums)]
            elif nums[index] > 0:
                result[index] = nums[(index + nums[index]) % len(nums)]
            else:
                result[index] = nums[index]
        return result