class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        
        # for a diagonal order, you have to realize that if you're on the same sum of rows and columns 

        # so maybe we can group by sum of (rows and columns)

        # and then just prioritize the one with the lowest row, so in the tuple in the heap (we can insert the sum, row, dont think you need the column)

        # okay, you technically don't need to do have a minHeap for this case, as you could technically just use a hashmap

        count = defaultdict(list)
        rows = len(nums)

        for row in range(rows):
            for col in range(len(nums[row])):
                sum_of_dimension = row + col
                count[sum_of_dimension].append(nums[row][col])   
             
        res = []
        currNum = 0

        while currNum in count:
            for item in reversed(count[currNum]):
                res.append(item)
            currNum += 1
        return res
