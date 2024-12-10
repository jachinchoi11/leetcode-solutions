class Solution:
    def maximumLength(self, s: str) -> int:
        count = defaultdict(int)

        for i in range(len(s)):
            special = True
            currString = ""
            for j in range(i, len(s)):
                if s[j] != s[i]:
                    break
                currString += s[j]
                count[currString] += 1
        
        currLength = 0
        for key, value in count.items():
            if value >= 3:
                currLength = max(currLength, len(key))
        return currLength if currLength != 0 else -1
                    
                