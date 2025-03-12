class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        # any negative number gets stopeed at its max absolute 
            # only if something is bigger in the stack 

        # so if it is possitive, it will never collide theoretically with any other positive


        stack = []
        negative_asteroid = []
        for asteroid in asteroids:

            if asteroid < 0:
            
                while stack and stack[-1] < abs(asteroid):
                        # case 1: where negative is bigger than the postiive ones
                    stack.pop()
                    
                if stack and stack[-1] == abs(asteroid):
                        # case 2: where they re equal and cancel each other out
                    stack.pop()
                    
                elif not stack:
                    # case 3: where negative wins all and gets to the very end 
                    negative_asteroid.append(asteroid)
            else:
                stack.append(asteroid)
        
        negative_asteroid.extend(stack)

        return negative_asteroid