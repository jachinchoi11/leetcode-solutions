class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pairs = []

        for index in range(len(position)):
            currPosition = position[index]
            currSpeed = speed[index]
            pairs.append((currPosition, currSpeed))
        
        pairs.sort(reverse = True)

        stack = []

        def computeTime(currCar, target):
            currTarget = target
            currTarget -= currCar[0]
            ans = currTarget / currCar[1]
            return ans
        
        for pair in pairs:
            if not stack:
                stack.append(pair)
            else:
                if computeTime(stack[-1], target) >= computeTime(pair, target):
                    continue
                else:
                    stack.append(pair)
        
        return len(stack)
        
