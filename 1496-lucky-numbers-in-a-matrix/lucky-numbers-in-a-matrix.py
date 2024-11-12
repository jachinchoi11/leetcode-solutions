class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        check = []
        res = []

        for row in range(m):
            minVal = float('inf')
            for col in range(n):
                minVal = min(minVal, matrix[row][col])
            check.append(minVal)
        
        for col in range(n):
            maxVal = 0
            for row in range(m):
                maxVal = max(maxVal, matrix[row][col])
            if maxVal in check:
                res.append(maxVal)
        
        return res
        
            


        