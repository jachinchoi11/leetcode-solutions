class MinStack:
    """
    For this problem , we want to initialize where to push the values 
    """
    def __init__(self):
        self.regStack = []
    def push(self, val: int) -> None:
        if self.regStack:
            minValue = min(self.regStack[-1][1], val)
            self.regStack.append((val, minValue))
        else:
            self.regStack.append((val, val))
    
    def pop(self) -> None:
        if self.regStack:
            self.regStack.pop()
        else:
            print("Nothing in the stack, so pop unsucessful")
        
    def top(self) -> int:
        if self.regStack:
            return self.regStack[-1][0]
        else:
            return []

    def getMin(self) -> int:
        return self.regStack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()