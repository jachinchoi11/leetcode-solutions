class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        # if we establish that one of them is not overlapping with the other, then it is immediatly wrong 
        maxValue = 0
        res = 0
        heap = []
        events.sort()
        
        for startTime, endTime, value in events:

            while heap and startTime > heap[0][0]:
                e, currValue = heapq.heappop(heap)
                maxValue = max(maxValue, currValue)

            res = max(maxValue + value, res)
            heapq.heappush(heap, (endTime, value))
            
        return res