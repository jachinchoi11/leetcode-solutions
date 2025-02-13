class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # i think we can use a heap to keep track of the top two minimum numbers 
        # and the number that we choose to do is to find how many there are 
        '''num_less_than_k = 0 
        minHeap = []
        operation_count = 0

        for num in nums:
            if num < k:
                num_less_than_k += 1
            heapq.heappush(minHeap, num)
        
        while len(minHeap) >= 2 and num_less_than_k > 0:
            num1 = heapq.heappop(minHeap)
            num2 = heapq.heappop(minHeap)
            num_less_than_k -= 2
            operation_count += 1
            newNum = (2 * min(num1, num2) + max(num1, num2))
            if newNum < k:
                num_less_than_k += 1
                heapq.heappush(minHeap, newNum)
            if num_less_than_k <= 0:
                break
        
        if minHeap and num_less_than_k > 0:
            operation_count += 1
        
        return operation_count'''

        minHeap = []
        operation_count = 0
        for num in nums:
            heapq.heappush(minHeap, num)
        
        while len(minHeap) >= 2 and minHeap[0] < k:
            operation_count += 1
            num1 = heapq.heappop(minHeap)
            num2 = heapq.heappop(minHeap)
            newNum = (2 * min(num1, num2) + max(num1, num2))
            heapq.heappush(minHeap, newNum)
        
        return operation_count

