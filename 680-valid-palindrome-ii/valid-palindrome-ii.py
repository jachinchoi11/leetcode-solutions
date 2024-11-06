class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        chance1 = False
        chance2 = False

        while left <= right:
            if s[left] != s[right]:
                chance1 = self.isPalindrome(left + 1, right, s)
                if chance1:
                    return True
                chance2 = self.isPalindrome(left, right - 1, s)
                if chance2:
                    return True
                else:
                    return False
            left += 1
            right -= 1
        
        return True
    

    def isPalindrome (self, left, right, s):

        while left <= right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True