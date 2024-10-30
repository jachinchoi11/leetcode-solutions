class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        nextValue = 0
        for i in range(1, numRows):
            ans = []
            ans.append(1)
            for j in range(1, i):
                nextValue = res[i - 1][j] + res[i-1][j-1]
                ans.append(nextValue)
            ans.append(1)
            res.append(ans)         
        return res


