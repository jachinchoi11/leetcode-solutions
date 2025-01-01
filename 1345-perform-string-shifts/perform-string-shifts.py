class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        queue = collections.deque(s)
        def shiftA(direction, amt):
            if direction == 1:
                for i in range(amt):
                    temp = queue.pop()
                    queue.appendleft(temp)
            else:
                for i in range(amt):
                    temp = queue.popleft()
                    queue.append(temp)
    
        for direction, amt in shift:
            shiftA(direction, amt)
        
        return "".join(list(queue))
