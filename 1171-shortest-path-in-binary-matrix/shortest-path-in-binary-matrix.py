class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # essntially we can from a bfs where we will have a quque of values 
        # satart from the topleft and essentialy get to the bottom right 
        # we're going to want traverse 8 direcitons bc it tells us we can do that
        # we can do this by using a nested for loop 
        # or we can set 8 directions using a 2d array and just map that out 
        # before we kind of decide to add it to the queue, there a coupel of cases we havet o avoiud 
        # one being going out of bounds so check for min(r,c) < 0 and also the r or c being cols - 1, rows -1 
        # lastly. if the value is 1 we don't want to explore the value 
        # we can have a length option that will allow us to essentilaly find the shortest length 

        queue = deque()
        length = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])

        if grid[0][0] == 1 or grid[rows - 1][cols - 1] == 1:
            return -1
        
        queue.append((0,0,1))

        while queue:
            curr = queue.popleft()
            neighbors = [[0, -1], [0, 1], [-1, 0], [1, 0], [-1,-1], [1,-1], [-1,1], [1, 1]]
            if curr[0] == rows - 1 and curr[1] == cols - 1:
                return curr[2]
            
            for dr, dc in neighbors:
                newR = dr + curr[0]
                newC = dc + curr[1]
                if newR < 0 or newC < 0 or newR >= rows or newC >= cols or grid[newR][newC] == 1 or (newR, newC) in visited:
                    continue
                queue.append((newR, newC, curr[2] + 1))
                visited.add((newR, newC))
            
        return -1
        
