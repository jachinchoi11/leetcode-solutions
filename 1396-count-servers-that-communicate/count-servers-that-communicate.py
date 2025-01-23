class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        

        # rows and cols hashmap 

        # and then just check if there is any in that row, i think we can do it as we go, and cancel out any 

        # the thing is when we actually do add stuff to each other, we dont want to remove anything, as it could not capture something later 

        # so i think a better way might just be to preprocess everythign int eh rows, cols hashmap 

        # check if there's at least more than one 


        rows, cols = len(grid), len(grid[0])

        rowsHash = defaultdict(list)
        colsHash = defaultdict(list)

        res = 0
        total_num = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    rowsHash[row].append(col)
                    colsHash[col].append(row)
                    total_num += 1
        potentialAns = []
        for key, value in rowsHash.items():
            # here we need to find places where there is only thing in a row, and then we can deduce if there is a col for it 
            if len(value) == 1:
                potentialAns.append(value[0])
        
        for ans in potentialAns:
            print(potentialAns)
            if len(colsHash[ans]) == 1:
                print(ans)
                res += 1
        
        return total_num - res


