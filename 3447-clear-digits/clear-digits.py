class Solution:
    def clearDigits(self, s: str) -> str:
        
        # so what if we had a stack that only took care of the non digits characters
        # when we see a character, pop off that index and add it to a hashset, then as we go through we don't use 
        index_set = set()

        stack = []

        for index, char in enumerate(s):
            if not char.isdigit():
                stack.append(index)
            else:
                if stack:
                    curr_index = stack.pop()
                    index_set.add(curr_index)
        
        res = []

        for index, char in enumerate(s):
            if char.isdigit() or index in index_set:
                continue
            res.append(char)
        return "".join(res)