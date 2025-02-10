class Solution:
    def clearDigits(self, s: str) -> str:
        
        # so what if we had a stack that only took care of the non digits characters
        # when we see a character, pop off that index and add it to a hashset, then as we go through we don't use 
        res = []

        for char in s:
            if not char.isdigit():
                res.append(char)
            else:
                if res:
                    res.pop()
                
        return "".join(res)