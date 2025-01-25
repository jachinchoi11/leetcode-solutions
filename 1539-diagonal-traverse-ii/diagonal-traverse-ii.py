class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        
        # for a diagonal order, you have to realize that if you're on the same sum of rows and columns 

        # so maybe we can group by sum of (rows and columns)

        # and then just prioritize the one with the lowest row, so in the tuple in the heap (we can insert the sum, row, dont think you need the column)


        minHeap = [] # will store the tuples of the sum and the rows 
        rows, cols = len(nums), len(nums[0])

        for row in range(rows):
            for col in range(len(nums[row])):
                heapq.heappush(minHeap, ((row + col), col, row))
        
        res = []

        while minHeap:
            _, col, row = heapq.heappop(minHeap)
            res.append(nums[row][col])
        
        return res
