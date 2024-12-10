class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        count = 0

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
        
        
        