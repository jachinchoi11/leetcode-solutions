class Solution:
    def makeFancyString(self, s: str) -> str:
        
        res = []
        count = 0
        currentChar = s[0]

        for char in s:
            if currentChar == char:
                count += 1
                if count >= 3:
                    continue
                res.append(char)
            else:
                count = 1
                currentChar = char
                res.append(char)
        
        return "".join(res)
            
        

