class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        count = defaultdict(int)

        total = 0
        for num in nums:
            total += count[num]
            count[num] += 1
        
        return total
        