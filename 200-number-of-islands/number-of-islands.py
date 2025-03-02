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
                    self.bfs(row, col, visited, rows, cols, grid)
                    num_of_islands += 1
        return num_of_islands

    def bfs(self, curr_row, curr_col, visited, rows, cols, grid):
            queue = deque([(curr_row, curr_col)])
            directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
            visited.add((curr_row, curr_col))
            def isValid(curr_row, curr_col):
                if curr_row < 0 or curr_col < 0 or curr_row == rows or curr_col == cols or grid[curr_row][curr_col] == '0' or (curr_row, curr_col) in visited:
                    return False
                return True 

            while queue:
                curr_row, curr_col = queue.popleft()
                for row_offset, col_offset in directions:
                    new_row = curr_row + row_offset
                    new_col = curr_col + col_offset
                    if isValid(new_row, new_col):
                        queue.append((new_row, new_col))
                        visited.add((new_row, new_col))
