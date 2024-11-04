class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        res = []
        if m * n != len(original):
            return []
        value = n
        currIndex = 0
        for tracker in range(m):
            curr = []
            while currIndex < value:
                curr.append(original[currIndex])
                currIndex += 1
            value = value + n
            res.append(curr)
        return res