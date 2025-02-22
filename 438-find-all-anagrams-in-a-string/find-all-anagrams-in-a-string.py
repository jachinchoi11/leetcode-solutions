class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        if len(s) < len(p):
            return []
        
        count_p = Counter(p)
        curr_count = defaultdict(int)
        res, left = [], 0

        # for this one, in an anagram it has to fit all the characters in the string case
        # so now, we have to figure out the case when we do find one, actually we don't need to 
        # since this is a fixed case we can do a fixed sliding window on this rpobem 

        for right in range(len(p)):
            curr_count[s[right]] += 1
        right += 1
        if curr_count == count_p:
            res.append(0)

        print(right) # tink about why you have to iterate right + 1, when you do this( has to do with logic of for loops)
        while right < len(s):
            right_char = s[right]
            curr_count[right_char] += 1
            left_char = s[left]
            left += 1
            curr_count[left_char] -= 1
            if curr_count[left_char] == 0:
                curr_count.pop(left_char)
            
            if curr_count == count_p:
                res.append(left)
            right += 1
        return res 