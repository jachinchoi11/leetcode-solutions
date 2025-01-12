class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # i think we can use a heap to keep track of the top two minimum numbers 
        # and the number that we choose to do 

        num_less_than_k = 0 
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
        
        return operation_count

        # 2,11,10,1,3
        # 1,2,3,10,11
        # num less = 2
        # operations = 2
        # 2,3,5,10, 11
        # 3,5,10,11,11
        #