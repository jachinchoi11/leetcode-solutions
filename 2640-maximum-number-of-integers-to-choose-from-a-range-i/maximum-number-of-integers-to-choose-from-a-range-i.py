class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        
        hashset = set(banned)
        currSum = 0
        count = 0

        for i in range(1,n + 1):
            if i in hashset:
                continue
            currSum += i
            if currSum <= maxSum:
                count += 1
            else:
                break
        return count
