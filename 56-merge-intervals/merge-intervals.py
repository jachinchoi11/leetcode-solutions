class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort() # by the start time 
        res = []
        for start, end in intervals:
            if res and start <= res[-1][1]:
                if res[-1][1] < end:
                    res[-1][1] = end
            else:
                res.append([start, end])
        return res

            