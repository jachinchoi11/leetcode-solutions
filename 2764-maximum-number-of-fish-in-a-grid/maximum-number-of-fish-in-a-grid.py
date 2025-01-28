class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        
        # so basically at every water cell, you can do a bfs, and then maximize the amount of fish taht are in it 



        rows, cols = len(grid), len(grid[0])

        queue = deque()
        maximum_fish = 0

        visited = set()

        def bfs(row, col):
            curr_count = 0
            queue.append((row ,col))
            visited.add((row, col))

            while queue:
                curr_row, curr_col = queue.popleft()
                curr_count += grid[curr_row][curr_col]
                for dr, dc in [[1, 0], [0, 1], [0, -1], [-1, 0]]:
                    newR = dr + curr_row
                    newC = dc + curr_col
                    if min(newR, newC) < 0 or newR == rows or newC == cols or (newR, newC) in visited or grid[newR][newC] == 0:
                        continue
                    queue.append((newR, newC))
                    visited.add((newR, newC))
            return curr_count        
    
        for row in range(rows):
            for col in range(cols):
                if (row, col) not in visited and grid[row][col] != 0:
                    maximum_fish = max(bfs(row, col), maximum_fish)
        
        return maximum_fish