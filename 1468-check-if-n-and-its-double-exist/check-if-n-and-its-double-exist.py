class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        visit = set()

        for index, curr in enumerate(arr):
            if curr * 2 in visit or curr / 2 in visit:
                return True
            visit.add(curr)
        return False