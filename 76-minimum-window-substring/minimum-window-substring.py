class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # if you're able to include all the characters of t 

        if len(s) < len(t):
            # Base case: the length of the t is lower than the s, not possible than
            return ""
        
        # so whenever you do these problems you can just discount from it 
        # and have some type of counter that will keep track of which conditions (in this case the amount of letters )

        res = []
        lowest_length = float('inf')
        currList = []

        left, right = 0, 0
        t_count = Counter(t)

        counter = len(set(t))

        while right < len(s):
            right_char = s[right]
            if right_char in t_count:
                t_count[right_char] -= 1
                if t_count[right_char] == 0:
                    counter -= 1

            while counter == 0:
                curr_length = (right - left + 1)
                if lowest_length > curr_length:
                    lowest_length = curr_length
                    res = [left, right]
                # then we can start subtracting 
                left_char = s[left]
                if left_char in t_count:
                    t_count[left_char] += 1
                    if t_count[left_char] == 1:
                        counter += 1
                left += 1
            right += 1
        
        return "".join(s[res[0]: res[1] + 1]) if res else ""


        # s = ab
        # t = a
        # you can not assume that it is the amount of unique characters


                



        