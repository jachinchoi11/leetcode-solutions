class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = []
        minLength = float('inf')
        for word in strs:
            minLength = min(len(word), minLength)

        for index in range(minLength):
            char = 0
            for i in range(len(strs)):
                if char == 0:
                    char = strs[i][index]
                elif char != strs[i][index]:
                    char = -1
                    break
            if char == -1:
                break
            res.append(char)
        return "".join(res)
            
