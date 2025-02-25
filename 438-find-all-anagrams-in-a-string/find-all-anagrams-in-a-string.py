class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        if len(s) < len(p):
            return []
        
        count_p = Counter(p)
        curr_count = defaultdict(int)
        res, left, right = [], 0, 0

        # for this one, in an anagram it has to fit all the characters in the string case
        # so now, we have to figure out the case when we do find one, actually we don't need to 
        # since this is a fixed case we can do a fixed sliding window on this rpobem 

        while right < len(s):
            right_char = s[right]
            curr_count[right_char] += 1

            if right >= len(p):
                # right will be 
                left_char = s[left]
                left += 1
                curr_count[left_char] -= 1
                if curr_count[left_char] == 0:
                    curr_count.pop(left_char)
            
            if curr_count == count_p:
                res.append(left)
            right += 1

        return res 