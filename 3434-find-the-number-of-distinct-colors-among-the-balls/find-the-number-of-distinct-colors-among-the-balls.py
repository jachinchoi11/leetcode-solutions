class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        
        # ok the main point of this problem is to check how many distinct colors there are 
        # so can't we just have a hashmap that keeps track of what ball --> color
        # but the only issue with just taking the len(hashmap) at the place, would be that there could be overlapping colors 
        # but we are looking for distinct colors, so that is something we have to keep account for 

        # what if we do use a hashmap to keep track of the frequencies of the color
            # whenever we replace a color that is already there 
            # we would reduce the color -= 1, and pop it if that value is 0
            # then take the len(of this hashmap)
            # otherwise, if the color is not in the other hashmap, we woudl add it into the ball
            # and just have to add the frequeqncy of it
        
        color_tracker = {}
        color_count = defaultdict(int)
        res = [0] * len(queries)
        for index, (ball, color) in enumerate(queries):
            if ball in color_tracker:
                past_color = color_tracker[ball]
                color_tracker[ball] = color
                color_count[past_color] -= 1
                if color_count[past_color] == 0:
                    color_count.pop(past_color)
                color_count[color] += 1
            else:
                color_tracker[ball] = color
                color_count[color] += 1
            res[index] = len(color_count)
        
        return res
        

