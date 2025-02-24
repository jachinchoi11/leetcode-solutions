class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        
        # you keep on going and delete when it is higher (condiition change )

        # in this case, it will be the same thing, where we can have a hashmap (count)

        

        left, right, res = 0, 0, 0

        curr_count = defaultdict(int)

        while right < len(s):
            right_char = s[right]
            curr_count[right_char] += 1

            while len(curr_count) > 2:
                left_char = s[left]
                curr_count[left_char] -= 1
                if curr_count[left_char] == 0:
                    curr_count.pop(left_char)
                left += 1
            
            res = max(res, right - left + 1)
            right += 1
        
        return res