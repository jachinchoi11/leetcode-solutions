class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = deque()

        l, r = 0, len(nums) - 1

        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                res.appendleft(nums[l])
                l += 1  
            else:
                res.appendleft(nums[r])
                r -= 1
        ans = []
        for index, num in enumerate(res):
            squaredNum = self.squareNumber(num)
            ans.append(squaredNum)           
        return ans
    def squareNumber(self, num):
        return num ** 2
