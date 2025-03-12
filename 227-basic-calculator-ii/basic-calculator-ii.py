class Solution:
    def calculate(self, s: str) -> int:
       

        # so i'm thinking of using a stack based approach, as fro the binary operators (+, - , *, /)
        # it requires two numbers right?

        # ill have an opeartor variabel that will keep track of what variable we are on 
            # if it is + 
                # just add the numebr
            
            # if it is - 
                # add the number negaive
            
            # if it is * 
                # then the old number * the new number we push in
            
            # if it is / 
                # then the older number / the new number we push in 
            
            # teh second loop will then just add it up (wil take care of + and -)

        
        operator = '+'
        s += '+'
        hashset = set('0123456789/*+-')
        stack = []
        res = 0
        current_num = 0
        for char in s:

            if char not in hashset:
                continue

            if char.isdigit():
                current_num = current_num * 10 + int(char)

            else:
                # only when it is a number, will it come here, otherwise we will just be able to change the operator
                if operator == '-':
                    stack.append(-current_num)
                elif operator == '*':
                    prev_num = stack.pop()
                    stack.append(prev_num * current_num)
                elif operator == '/':
                    prev_num = stack.pop()
                    stack.append(int(prev_num / current_num))
                elif operator == '+':
                    stack.append(current_num)

                operator = char
                current_num = 0
            


        return sum(stack)
        
        


            
