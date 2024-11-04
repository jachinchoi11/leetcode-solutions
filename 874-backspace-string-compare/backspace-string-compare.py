class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool: 
        res = []
        for char in s:
            if res and char == '#':
                res.pop()
            elif char != '#':
                res.append(char)
        res1 = []
        for char in t:
            if res1 and char == '#':
                res1.pop()
            elif char!= '#':
                res1.append(char)
        return res1 == res
        