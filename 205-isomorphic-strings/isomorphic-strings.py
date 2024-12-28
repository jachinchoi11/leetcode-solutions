class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        # so i think the way we can go about this using a hashmap
        # it also does say that you can not map two letters to the same thing 
        # i assume that you can just map the letters to the t letters
        # if it is already present in the 

        switch = {}
        hashset = set()

        for charS, charT in zip(s, t):
            if charS not in switch:
                if charT in hashset:
                    return False
                switch[charS] = charT
            else:
                if switch[charS] == charT:
                    continue
                else:
                    return False
            hashset.add(charT)
        return True