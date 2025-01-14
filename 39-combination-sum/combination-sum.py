class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res, currList = [], []

        def backtrack(i, currSum):
            # backtracking logic base cases 
            if currSum > target:
                return
            if currSum == target:
                res.append(currList[:])
                return
            
            print(currList)
            # what do we need to try, everytime we go we have to try all possibilities 

            for index in range(i, len(candidates)):
                currList.append(candidates[index])
                currSum += candidates[index]

                backtrack(index, currSum)

                currSum -= candidates[index]
                currList.pop()
            
        backtrack(0, 0)
        return res