class Solution:
    def hasSameDigits(self, s: str) -> bool:
        current_length = len(s)
        input_string = s

        while current_length > 2:
            input_string = self.computeNew(input_string)
            current_length = len(input_string)
        return True if input_string[0] == input_string[1] else False
    
    def computeNew(self, input_string):
        pointer = 0
        res = []

        while pointer < len(input_string) - 1:
            first_char = input_string[pointer]
            second_char = input_string[pointer + 1]
            number = (int(first_char) + int(second_char)) % 10
            res.append(str(number))
            pointer += 1
        
        return "".join(res)
