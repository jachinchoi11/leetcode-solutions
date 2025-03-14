class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        # yeah to build the longest palindrome in this case, we can first count the frequencies of all the chars
        # if it is even we can always use it, and thne we want to use the highest odd one

        count_map = Counter(s)
        res = 0
        has_odd = False

        for frequency in count_map.values():
            if frequency % 2 == 0:
                res += frequency
            else:
                res += (frequency - 1)
                has_odd = True
        
        return res + 1 if has_odd else res