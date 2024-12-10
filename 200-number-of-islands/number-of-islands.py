class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # dfs solution
        '''count = 0

        def dfs(row, col):   
            if min(row, col) < 0 or row == len(grid) or col == len(grid[0]) or grid[row][col] != '1':
                return
            grid[row][col] = '0'

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)


        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '0':
                    continue
                dfs(row, col)
                count += 1
        return count
        
        
        '''
        # bfs solution 

        num_of_islands = 0
        rows, cols = len(grid), len(grid[0])
        queue = deque()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '0':
                    continue
                queue.append((row, col))
                grid[row][col] == '0'
                while queue:
                    currRow, currCol = queue.popleft()
                    adj = [[1,0], [0,1], [-1,0], [0,-1]]
                    for dx, dy in adj:
                        newRow = currRow + dx
                        newCol = currCol + dy
                        if min(newRow, newCol) < 0 or newRow == rows or newCol == cols or grid[newRow][newCol] == '0':
                            continue
                        queue.append((newRow, newCol))
                        grid[newRow][newCol] = '0'
                num_of_islands += 1
        return num_of_islands

        
