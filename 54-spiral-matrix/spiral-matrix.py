class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, bottom = 0, len(matrix)
        left, right = 0, len(matrix[0])

        res = []
        while top < bottom and left < right:
            # first way to go about this is first go from top left to top right

            for index in range(left, right):
                res.append(matrix[top][index])
            top += 1
            if top >= bottom:
                break
            # now go from top right to bottom right

            for index in range(top, bottom):
                res.append(matrix[index][right - 1])
            right -= 1
            if left >= right:
                break

            # now go from bottom right to bottom left

            for index in range(right - 1, left -1, -1):
                res.append(matrix[bottom - 1][index])
            bottom -= 1
            if top >= bottom:
                break
            # now go from bottom left to top left

            for index in range(bottom - 1, top - 1, -1):
                res.append(matrix[index][left])
            left += 1
            if left >= right:
                break      
        return res

            


