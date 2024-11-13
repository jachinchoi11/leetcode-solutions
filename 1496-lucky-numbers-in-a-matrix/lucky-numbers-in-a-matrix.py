class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        check = []
        res = []
        maxminVal = 0
        minmaxVal = float('inf')
        for row in range(m):
            minVal = float('inf')
            for col in range(n):
                minVal = min(minVal, matrix[row][col])
            maxminVal = max(minVal, maxminVal)
        
        for col in range(n):
            maxVal = 0
            for row in range(m):
                maxVal = max(maxVal, matrix[row][col])
            minmaxVal = min(maxVal, minmaxVal)
        if minmaxVal == maxminVal:
            return [minmaxVal]
        return []
        
            


        