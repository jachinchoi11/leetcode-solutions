class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        count = 0
        queue = deque()
        currTime = -1
        visited = set()
        time = 1
        rows = len(grid)
        cols = len(grid[0])
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    count += 1
                elif grid[row][col] == 2:
                    queue.append([row, col])
                    visited.add((row, col))
        
        if count == 0:
            return 0
        while queue:
            for _ in range(len(queue)):
                currRow, currCol = queue.popleft()
                neighbors = [[0,1], [1,0], [-1,0], [0,-1]]
                for dr, dc in neighbors:
                    newR = currRow + dr
                    newC = currCol + dc
                    if min(newR, newC) < 0 or newR == rows or newC == cols or grid[newR][newC] != 1:
                        continue
                    grid[newR][newC] = 2
                    queue.append([newR, newC])
                    count -= 1
                    if count == 0:
                        return time
            time += 1
        return -1 
                
        
            
        # so we have a count no 