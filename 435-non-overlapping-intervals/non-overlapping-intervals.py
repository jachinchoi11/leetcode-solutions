class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key = lambda x: (x[1], x[0]))
        last_end = -float('inf')
        res = 0
        
        for start, end in intervals:
            if start >= last_end:
                last_end = end
            else:
                res += 1
        return res
