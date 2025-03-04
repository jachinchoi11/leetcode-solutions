class Solution:
    def sumRemoteness(self, grid: List[List[int]]) -> int:
        # this doesn't look too difficult
        # i think traverse through the array and find the sum of everything (not including the blocked -1 values)
        # then any time, we encounter a non blocked value, we do a dfs of anythign it can make a path to and subtract it from the total sum 


        rows, cols = len(grid), len(grid[0])
        total_sum = 0
        result = 0 

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] != -1:
                    total_sum += grid[row][col]

        def isValid(row, col):
            if min(row, col) < 0 or row == rows or col == cols or (row, col) in visited or grid[row][col] == -1:
                return False
            return True
        
        def dfs(row, col, arr):
        
            visited.add((row, col))
            arr[0] += 1
            arr[1] += grid[row][col]

            for dr, dc in [[0, 1] , [1, 0], [-1, 0], [0, -1]]:
                newR = dr + row
                newC = dc + col
                if isValid(newR, newC):
                    dfs(newR, newC, arr)
            return arr

        visited = set()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] != - 1 and (row, col) not in visited:
                    amt, value = dfs(row, col, [0, 0])
                    result += amt * (total_sum - value)
        return result

        


