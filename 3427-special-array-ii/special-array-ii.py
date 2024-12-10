class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        res = [False] * len(queries)
        # we have to do prefix sums in this case and compute which how many bad indexes there are 

        prefixSum = [0] * len(nums)

        for index in range(1, len(nums)):
            if nums[index] % 2 == nums[index - 1] % 2:
                prefixSum[index] = prefixSum[index - 1] + 1
            else:
                prefixSum[index] = prefixSum[index - 1]
        
        currIndex = 0
        for start, end in queries:
            if prefixSum[end] - prefixSum[start] == 0:
                res[currIndex] = True
            else:
                res[currIndex] = False
            currIndex += 1
        return res
            
