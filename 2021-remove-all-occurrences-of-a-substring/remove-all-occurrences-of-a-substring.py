class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:

        current_arr = []

        for char in s:
            current_arr.append(char)
            if len(current_arr) >= len(part):
                if "".join(current_arr[-len(part):]) == part:
                    print("hello")
                    for i in range(len(part)):
                        current_arr.pop()
        
        return "".join(current_arr)
