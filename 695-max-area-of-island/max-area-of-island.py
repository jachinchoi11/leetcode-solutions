class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(row, col):
            if row < 0 or col < 0 or row == rows or col == cols or grid[row][col] == 0:
                return     
            grid[row][col] = 0
            self.currLength += 1

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        maxLength = 0
        rows, cols = len(grid), len(grid[0])

        for row in range(rows):
            for col in range(cols):
                self.currLength = 0
                if grid[row][col] == 1:
                    dfs(row, col)
                    maxLength = max(maxLength, self.currLength)
        return maxLength
