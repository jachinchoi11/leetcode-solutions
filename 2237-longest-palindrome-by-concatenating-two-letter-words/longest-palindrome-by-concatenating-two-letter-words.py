class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
    
        count = {}
        res = 0
        # account for the edge case if the two leetters are the same just add it
        for word in words:
            currString = ""
            currString += word[1]
            currString += word[0]
            if currString in count:
                res += 4
                count[currString] -= 1
                if count[currString] == 0:
                    count.pop(currString)
            else:
                if word in count:
                    count[word] += 1
                else:
                    count[word] = 1
        
        for word in count:
            if word[0] == word[1]:
                res += 2
                break
        return res 

