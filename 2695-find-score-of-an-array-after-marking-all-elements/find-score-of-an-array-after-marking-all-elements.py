class Solution:
    def findScore(self, nums: List[int]) -> int:
        # you can use a minheap and just simulate this out
        minHeap = []
        hashset = set()
        res = 0
        for index, value in enumerate(nums):
            heapq.heappush(minHeap, (value, index))
        
        while minHeap:
            currValue, currIndex = heapq.heappop(minHeap)
            if currIndex not in hashset:        
                res += currValue
                hashset.add(currIndex)
                if currIndex == 0:
                    hashset.add(currIndex + 1)
                elif currIndex == len(nums) - 1:
                    hashset.add(currIndex - 1)
                else:
                    hashset.add(currIndex + 1)
                    hashset.add(currIndex - 1)
        return res
