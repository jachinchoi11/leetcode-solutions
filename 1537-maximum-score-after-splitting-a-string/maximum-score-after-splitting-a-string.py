class Solution:
    def maxScore(self, s: str) -> int:
        # we can just use sliding windo in this case 
        # we can slide from the frequency of 0s that are in the current substring
        # we first should count how many 1s and 0s there are 
        # well keep a count of how many 0s in the left substring
        # and when we iterate the sliding windo we can add how many 1s there are 

        count = defaultdict(int)
        for char in s:
            if char == '1':
                count[char] += 1
        res, pointer = 0, 0

        while pointer < len(s) - 1:
            if s[pointer] == "0":
                count[s[pointer]] += 1
            else:
                count[s[pointer]] -= 1
            res = max(res, count["0"] + count["1"])
            pointer += 1
        
        return res  
