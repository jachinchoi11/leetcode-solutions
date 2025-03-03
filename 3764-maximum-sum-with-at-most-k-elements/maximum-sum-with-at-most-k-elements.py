class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        
        # top limits[i] elements in each row of the grid 
            # depending on the limit i, so we can just do a reverse sort 
            # heapq.heappush -> it onto the heap 
        
        # and then with the k value we can get the top k elements from that 


        # would be to preprocess each of teh array and reverse sort 

        rows = len(grid)
        heap = []
        res = 0
        for row in range(rows):
            grid[row].sort(reverse = True)
            for value in range(limits[row]):
                heapq.heappush(heap, -grid[row][value])
        
        while k > 0:
            num = -heapq.heappop(heap)
            res += num
            k -= 1
        return res
        
        
            
        

        
