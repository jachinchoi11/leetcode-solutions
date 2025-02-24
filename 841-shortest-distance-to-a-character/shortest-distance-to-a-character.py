class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        # find all the occurences of the indexes  
        # we can double pass this and just find the minimum values, lowkey 

        # one way, we can have a stack that carried the latest index and you can calcualte that 
        # and the pass again, and see if its min 

        res = [float('inf')] * len(s)
        most_recent_left = -1
        for index, char in enumerate(s):
            if char == c:
                most_recent_left = index
            if most_recent_left != -1:
                res[index] = abs(most_recent_left - index)
        
        most_recent_left = -1
        for index, char in enumerate(reversed(s)):
            if char == c:
                most_recent_left = index
            if most_recent_left != -1:
                res[-index - 1] = min(abs(most_recent_left - index), res[-index-1])
        
        return res

        