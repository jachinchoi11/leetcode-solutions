class Solution:
    def maximumLength(self, s: str) -> int:
        
        count = defaultdict(int)
        currString = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                special = True
                if len(set(s[i:j + 1])) != 1:
                    special = False
                if special:
                    count[s[i:j + 1]] += 1
        print(count)  
        currLength = 0
        for key, value in count.items():
            if value >= 3:
                currLength = max(currLength, len(key))
        return currLength if currLength != 0 else -1
                    
                