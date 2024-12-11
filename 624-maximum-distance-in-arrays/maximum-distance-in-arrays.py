class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        # woudln't it be to find the minimum of one and then jsut find the maximum in anotehr 
        minHeap = []
        maxHeap = []
        for index in range(len(arrays)):
            for num in arrays[index]:
                heapq.heappush(minHeap, (num, index))
                heapq.heappush(maxHeap, (-num, index))
        minNumber, index1 = heapq.heappop(minHeap)
        maxNumber, index2 = heapq.heappop(maxHeap)

        res = 0
        if index1 != index2:
            return abs(-1 * maxNumber - minNumber)
        for i in range(len(minHeap)):
            currMax, currMaxIndex = heapq.heappop(maxHeap)
            currMin, currMinIndex = heapq.heappop(minHeap)
            if currMaxIndex != index1:
                currDiff1 = abs(-1 * currMax - minNumber)
                res = max(currDiff1, res)
            if currMinIndex != index2:
                currDiff2 = abs(-1 * maxNumber - currMin)
                res = max(currDiff2, res)
        
        return res
                