class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        # to the foward is 1, backward is 0 
        # as in shifting the ascii values of the word 

        # i think the optimal approach would be to find converging ones 
        # and merge the shifts first 
        # and then do it, but also you coudl just go as you go
        # easier to do, the approach will be that we will essentially just go through the shifts and make the changes 
        # so let's first make all the queries 
        # if you are inclusive of start and end times 
        diff = [0] * (len(s))
        res = ""
        letters = "abcdefghijklmnopqrstuvwxyz"
        for start, end, direction in shifts:
            if direction == 0:
                diff[start] -= 1
                if end + 1 == len(diff):
                    continue
                diff[end + 1] += 1
            else:
                diff[start] += 1
                if end + 1 == len(diff):
                    continue
                diff[end + 1] -= 1
        currChange = 0

        for change, char in zip(diff, s):
            currChange += change
            curr_add_letter_index = (ord(char) - ord('a') + currChange) % 26
            res += letters[curr_add_letter_index]
        return res

