class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        for index in range(len(stones)):
            stones[index] = -stones[index]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = -heapq.heappop(stones)
            second = -heapq.heappop(stones)
            if first == second:
                continue
            else:
                diff = first - second 
                heapq.heappush(stones, -diff)
        if stones:
            return -stones[0]
        else:
            return 0
        


