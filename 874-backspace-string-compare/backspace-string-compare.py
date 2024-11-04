class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        counterS = 0
        resS = []
        resT = []
        index = len(s) -1
        counterS = 0
        while index >= 0:
            if s[index] == "#":
                counterS += 1
            elif counterS > 0:
                counterS -= 1
            else:
                resS.append(s[index])
            index -= 1
        index = len(t) - 1
        counterT = 0
        while index >= 0:
            if t[index] == '#':
                counterT += 1
                
            elif counterT > 0:
                counterT -= 1
            else:
                resT.append(t[index])
            index -= 1
        print(resT)
        print(resS)
        return resT == resS


