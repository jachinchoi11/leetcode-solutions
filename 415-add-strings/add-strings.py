class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        carry = 0
        res = []
        char1, char2 = len(num1) - 1, len(num2) - 1

        while char1 >= 0 and char2 >= 0:
            curr_place = int(num1[char1]) + int(num2[char2])
            if carry > 0:
                curr_place += carry
                carry = 0
            while curr_place > 9:
                curr_place -= 10
                carry += 1
            res.append(str(curr_place))
            char1 -= 1
            char2 -= 1
        
        while char1 >= 0:
            curr_place = int(num1[char1])
            if carry > 0:
                curr_place += carry
                carry = 0 
            while curr_place > 9:
                curr_place -= 10
                carry += 1
            char1 -= 1
            res.append(str(curr_place))
        
        while char2 >= 0:
            curr_place = int(num2[char2])
            if carry > 0:
                curr_place += carry
                carry = 0
            while curr_place > 9:
                curr_place -= 10
                carry += 1
            char2 -= 1
            res.append(str(curr_place))

        if carry > 0:
            res.append(str(carry))   
        
        return "".join(reversed(res))
            