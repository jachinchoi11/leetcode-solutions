class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            if num in count:
                count[num] -= 1
            else:
                count[num] = -1
            
        heap = []
        for key, value in count.items():
            heapq.heappush(heap, (value, key))
        res = []
        for i in range(k):
            value = heapq.heappop(heap)
            res.append(value[1])
        
        return res 



