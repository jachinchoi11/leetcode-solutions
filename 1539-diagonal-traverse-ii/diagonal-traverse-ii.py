class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        '''        
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
        return res'''

        # a really cool bfs approach that would be one pass, essentially you would bfs into the right and the bottom directions and append as you go 
        # make sure to prioritize the downward first and then also have a visited set 

        queue = deque()
        queue.append((0, 0))
        visited = set()
        res = []

        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                for dr, dc in [[1, 0], [0, 1]]:
                    newR = dr + row
                    newC = dc + col
                    if newR >= len(nums) or newC >= len(nums[newR]):
                        continue
                    if (newR, newC) not in visited:
                        queue.append((newR, newC))
                        visited.add((newR, newC))
                res.append(nums[row][col])
        return res
