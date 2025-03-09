class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = [] # going to carry the indexes (to calcualte width) and the hieghts
        # will be monotonic in nature and increasing


        for index, curr_height in enumerate(heights):
            placement_index = index

            while stack and stack[-1][0] > curr_height:
                prev_height, prev_index = stack.pop()
                max_area = max(max_area, prev_height * (index - prev_index))
                placement_index = prev_index
            
            stack.append([curr_height, placement_index])

        for height, index in stack:
            max_area = max(max_area, height * (len(heights) - index))
        
        return max_area
        




