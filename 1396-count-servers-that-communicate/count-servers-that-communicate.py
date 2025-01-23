class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        

        # rows and cols hashmap 

        # and then just check if there is any in that row, i think we can do it as we go, and cancel out any 

        # the thing is when we actually do add stuff to each other, we dont want to remove anything, as it could not capture something later 

        # so i think a better way might just be to preprocess everythign int eh rows, cols hashmap 

        # check if there's at least more than one 


        rows, cols = len(grid), len(grid[0])

        rowsHash = defaultdict(int)
        colsHash = defaultdict(int)

        res = 0
        total_num = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    rowsHash[row] += 1
                    colsHash[col] += 1
                    total_num += 1
                    
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and rowsHash[row] == 1 and colsHash[col] == 1:
                    res += 1

        
        return total_num - res


