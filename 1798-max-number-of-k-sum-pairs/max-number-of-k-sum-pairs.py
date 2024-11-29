class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        res = 0
        for num in nums:
            target = k - num
            if target in count:
                count[target] -= 1
                res += 1
                if count[target] == 0:
                    count.pop(target)
            else:
                count[num] += 1
        return res
        