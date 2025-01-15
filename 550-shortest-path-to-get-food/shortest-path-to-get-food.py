class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        '''
        - do a bfs from the person to the food squares 
        - we can have a timer that we'll add one for each bfs 
        - make an isValid function to check if you can do a certain function
            - the valid would be being inside the bounds, not being a X
        - the base case is hwen it reaches the *, we would just return the time of it 

        - at the beginning, we would have to go through the grid and find the starting loacation 
            - when it hits * cell
        
        - also account fo the fact taht if we don't see anything than we return -1, 
            - essentially, all we have to do in this case would be to return -1 on the outside 
        '''

        # find the starting location in the grid(*)

        rows, cols = len(grid), len(grid[0])
        queue = deque()
        visited = set()

        time_required = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '*':
                    queue.append((row, col))
                    visited.add((row, col))
                    break
        
        while queue:
            time_required += 1
            for _ in range(len(queue)):
                currRow, currCol = queue.popleft()
                directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
                for dr, dc in directions:
                    newR = dr + currRow
                    newC = dc + currCol

                    if newR < 0 or newC < 0 or newR == rows or newC == cols or grid[newR][newC] == 'X' or (newR, newC) in visited:
                        continue
                    if grid[newR][newC] == '#':
                        return time_required
                    queue.append((newR, newC))
                    visited.add((newR, newC))
        return -1


