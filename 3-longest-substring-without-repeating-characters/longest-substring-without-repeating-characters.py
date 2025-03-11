class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # so our limiting case is having duplicate characters, so basically, we can not have that

        # we could try every single substring (O(n^2)) --> which is almost certainly too slow for larger strings
        
        # a more optimal approach would be to use a sliding window, where we can dynamically shift our window until it has only unique characters
            # whenever we encoujnter a character we have already seen before 
                # easy check with a hashmap/set
                # we wil shrink our array until it doesn't have the duplpicate character
        
        # then we will have a var that can encompass everything 

        left, right, max_length = 0, 0, 0
        freq_count = defaultdict(int)

        while right < len(s):
            curr_char = s[right]

            while curr_char in freq_count:
                left_char = s[left]
                freq_count[left_char] -= 1
                if freq_count[left_char] == 0:
                    del freq_count[left_char]
                left += 1
            
            freq_count[curr_char] += 1
            max_length = max(max_length, right - left + 1)
            right += 1
        return max_length

