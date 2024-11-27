class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixSum = [0] * len(nums)
        currSum = 0
        for index, num in enumerate(nums):
            currSum += num
            self.prefixSum[index] = currSum
        print(self.prefixSum)
    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefixSum[right]
        return self.prefixSum[right] - self.prefixSum[left - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)