class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        res = []
        intervals.sort()
        for start, end in intervals:
            if res:
                if start <= res[-1][1]:
                    if res[-1][1] < end:
                        res[-1][1] = end
                else:
                    res.append([start,end])
            else:
                res.append([start, end])
        
        return res