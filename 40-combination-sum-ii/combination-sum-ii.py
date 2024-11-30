class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res, currList = [], []
        candidates.sort()
        def backtrack(index, remainingSum):

            if remainingSum == 0:
                res.append(currList[:])
                return
            if remainingSum < 0:
                return
            
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                currList.append(candidates[i])
                backtrack(i + 1, remainingSum - candidates[i])
                currList.pop()
        backtrack(0, target)
        return res



        