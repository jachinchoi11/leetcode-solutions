class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        currList, res = [], []

        count = {'2': ['a','b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9':['w', 'x', 'y', 'z']}
        if len(digits) == 0:
            return []

        def backtrack(index):
            
            if len(currList) == len(digits):
                res.append("".join(currList))
                return 

            num = count[digits[index]]

            for number in num:
                currList.append(number)
                backtrack(index + 1)
                currList.pop()

        backtrack(0)
        return res