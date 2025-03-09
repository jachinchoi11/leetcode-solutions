class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # there are n cars reaching target
            # they have diff sppedds and diff positions
        
        # limitation --> the car ahead of you if your speed is faster than thiers
            # switch speeds to the car slower
         
        # if the limitation is that, we should calculate, when they would get to said target
            # if you get there faster or same speed as someone ahead of you 
                # then you become a fleet together 
        
        # maybe a good solution would be to start with the people that get thier first 
            # we would have a stack of tuples 
        
        pairs = [(curr_position, curr_speed) for curr_position, curr_speed in zip(position, speed)]
        pairs.sort(reverse = True)

        stack = []

        for curr_p, curr_s in pairs:
            curr_time = self.calculate_time(curr_p, curr_s, target)
            if not stack:
                stack.append(curr_time)
            else:
                if stack[-1] < curr_time:
                    stack.append(curr_time)
        
        return len(stack)

    def calculate_time(self, curr_p, curr_s, target):
        return (target - curr_p) / curr_s