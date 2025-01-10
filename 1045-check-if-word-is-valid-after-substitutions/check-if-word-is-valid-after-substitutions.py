class Solution:
    def isValid(self, s: str) -> bool:
        
        # maybe we can have a stack that keeps track of how many 'abc' you have as you go trhough the string 
        
        stack = []

        for char in s:
            if len(stack) >= 2:
                if char == 'c' and stack[-1] == 'b' and stack[-2] == 'a':
                    stack.pop()
                    stack.pop()
                else:
                    stack.append(char)
            else:
                stack.append(char)
        
        return True if not stack else False