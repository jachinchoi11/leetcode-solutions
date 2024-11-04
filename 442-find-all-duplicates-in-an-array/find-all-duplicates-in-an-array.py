class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # essentiallly, you would multiply the index by -1, if you multiply the number and it is -1, that means there is duplicate
        res = []
        for index in range(len(nums)):
            number = abs(nums[index])
            if nums[number - 1] < 0:
                res.append(abs(number))
            nums[number - 1] = -1 * nums[number - 1]
        return res
