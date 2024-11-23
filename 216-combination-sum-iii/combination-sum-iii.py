class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        usedList = []

        for i in range(1, 10):
            usedList.append(i)
        
        res, currList = [], []

        def backtrack(index, remainingSum):
            if len(currList) == k:
                if remainingSum == 0:
                    res.append(currList[:])
                return
            
            for i in range(index, len(usedList)):
                if usedList[i] not in currList:
                    currList.append(usedList[i])
                    backtrack(i, remainingSum - usedList[i])
                    currList.pop()        
        
        backtrack(0, n)
        return res
