class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        # we can just brute force and simulate it and check whether the whole row is filleld 

        # have two hashmaps: one for row and one for col 

        # i think you have to take advantage of the fact that all the integers from  to m * n will be present

        # keep a counter of what the rows and cols are, defaultdict(int) are filed 
        # two hashmaps,  and update, when you add, check if it equals the len(mat) for row or len(mat[0]) for col


        coord = {}
        rows, cols = len(mat), len(mat[0])

        rowCounter, colCounter = [0] * len(mat), [0] * len(mat[0])
    
        for i in range(rows):
            for j in range(cols):
                value = mat[i][j]
                coord[value] = (i, j)
        
        for index, num in enumerate(arr):
            i, j = coord[num]
            rowCounter[i] += 1
            colCounter[j] += 1

            if rowCounter[i] == cols or colCounter[j] == rows:
                return index
        
        return 
        






