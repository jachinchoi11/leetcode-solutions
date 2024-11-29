class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # wait this is easy as balls
        # first step should be to have one stack 
        # essentially if you ever seem a divisor get the last two numbers and do division 
        # make sure to save both numbers and second uyou pop is first value etc


        stack = []
        hashset = set('+-/*')

        for value in tokens:
            if value not in hashset:
                stack.append(int(value))
            else:
                resultValue = 0
                secondValue = stack.pop()
                firstValue = stack.pop()
                if value == '+':
                    resultValue = firstValue + secondValue
                elif value == '-':
                    resultValue = firstValue - secondValue
                elif value == '*':
                    resultValue = firstValue * secondValue
                else:
                    resultValue = int(firstValue/secondValue)
                stack.append(resultValue)
        return stack[0]


