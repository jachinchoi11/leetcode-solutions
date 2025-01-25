class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # maybe we can do the 2 pass way 


        sum_rc = defaultdict(list)
        rows, cols = len(mat), len(mat[0])

        for row in range(rows):
            for col in range(cols):
                curr_sum = row + col
                sum_rc[curr_sum].append(mat[row][col])
        
        res = []

        curr = 0
        opposite = True
        while curr in sum_rc:
            if opposite:
                for i in reversed(sum_rc[curr]):
                    res.append(i)
            else:
                res.extend(sum_rc[curr])
            opposite = not opposite
            curr += 1
        
        return res