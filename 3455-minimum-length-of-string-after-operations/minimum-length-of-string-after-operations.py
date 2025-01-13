class Solution:
    def minimumLength(self, s: str) -> int:
        # i dont think we actually have to do anything 
        # we just have to count the frequency and take out if the freq at least 3 and add 1 to count 


        count = Counter(s)
        res = len(s)

        for value in count.values():
            while value >= 3:
                value -= 2
                res -= 2
        return res
            
