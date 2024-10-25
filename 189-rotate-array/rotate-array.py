class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        res = [0] * len(nums)
        n = len(nums)
        for index in range(n):
            res[(index + k) % n] = nums[index]  
        nums[:] = res