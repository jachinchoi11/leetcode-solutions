class Solution:
    def decodeString(self, s: str) -> str:

        # decoding a string 
        # we can use a stack because everythign has to be processed inside first 
        # so we will parse through the string s, and only add if it is a number orpart o fthe alphabet
        # then pop it off and put it into a res 
        # however, we have to find a way if it is nested or not 
        # we have to keep track of the [ and ]
        # we can save the currentNumber on a stack 
        # process that once that comes up 

        stack = []

        for char in s:
            if char == ']':
                currentString = ""
                while stack[-1] != '[':
                    currentChar = stack.pop()
                    currentString = currentChar + currentString
                _ = stack.pop()
                currentNum = ""
                while stack and stack[-1].isdigit():
                    currentNum = stack.pop() + currentNum
                decodedString = currentString * int(currentNum)
                stack.append(decodedString)
            else:
                stack.append(char)
        return "".join(stack)