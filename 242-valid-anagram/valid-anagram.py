class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = defaultdict(int)
        

        for char in s:
            countS[char] += 1
        for char in t:
            countS[char] -= 1
        
        for value in countS.values():
            if value != 0:
                return False
        return True