class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        MOD = (10**9) + 7

        minHeap = []

        for num in nums:
            heapq.heappush(minHeap, num)

        
        while k > 0:
            curr = heapq.heappop(minHeap)
            heapq.heappush(minHeap, curr + 1)
            k -= 1
        res = 1
        for num in list(minHeap):
            res *= num
        
        return res % MOD

