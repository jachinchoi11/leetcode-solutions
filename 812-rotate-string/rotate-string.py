class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        doubled = s + s

        if goal in doubled:
            return True
        return False
                
                