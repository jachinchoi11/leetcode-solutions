class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # first clarifying questions I want to ask is the input always going to be in a 2d array
        # and theo nly possibilities are land and water?

        # to define what an isalnd, its land tht is adjacent to each other 
            # what about diagonals, does diagonals count as adjacent ? no
        
        # one more thign is this input going to be resued somewhere else (in a followup)
            # i thin kwe can save sapce and alter the grid while we go through it or use some type of visited set potentially 

        # bfs: where we can kind of just go trhough the 2d grid and whenever we do see a 1 
            # we can just look at it and see if it is in our visited if not 
                # the we call the bfs 
                # eveyrtime we call the bfs, we would increment our count of islands by 1
        
        # inside the bfs: we woudl esssetnailyl - check all teh 4 direcitons and look at if there are any 1s
            # when we're checking all 4 firecitons, we have to mkae sure it is in bounds as well 
            # add it to the qeue and the visited set (so it can conitnue to check all adjacent ones)
        

        num_of_islands = 0
        rows, cols = len(grid), len(grid[0])
        visited = set()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1' and (row, col) not in visited:
                    self.dfs(row, col, visited, rows, cols, grid)
                    num_of_islands += 1
        return num_of_islands

    def dfs(self, row, col, visited, rows, cols, grid):
        def isValid(row, col):
            if row < 0 or col < 0 or row == rows or col == cols or grid[row][col] == '0' or (row, col) in visited:
                return False
            return True
        
        if not isValid(row, col):
            return
        
        visited.add((row, col))

        self.dfs(row + 1, col, visited, rows, cols, grid)
        self.dfs(row - 1, col, visited, rows, cols, grid)
        self.dfs(row, col + 1, visited, rows, cols, grid)
        self.dfs(row, col - 1, visited, rows, cols, grid)
    


