class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        hashset = set(nums)
        currList, res = [], []
        options = ["0", "1"]

        def backtrack(current_length, index):
            if len(res) > 0:
                return
            if current_length == len(nums):
                if "".join(currList) not in hashset:
                    res.append("".join(currList))
                return
            
            for index in range(len(options)):
                currList.append(options[index])
                backtrack(len(currList), index + 1)
                currList.pop()
            
        backtrack(0, 0)
        return res[0] if res else None