class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        '''
        can we just assign it in a hashmap with the values
        '''

        res = [[] for _ in range(numRows)]
        convert = []
        pointer = 0
        increasing = True
        index = 0

        if numRows == 1 or numRows >= len(s):
            return s
        
        for char in s:
            res[pointer].append(char)
            if increasing:
                pointer += 1
            else:
                pointer -= 1
            if pointer == numRows - 1:
                increasing = False
            if pointer == 0:
                increasing = True
        for each_list in res:
            convert.extend(each_list)
        return "".join(convert)
            



