class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        currRooms = 0
        maxRooms = 0
        maxTime = 0

        for _, end in intervals:
            maxTime = max(maxTime, end)
        ans = [0] * (maxTime + 1)
        currRooms = 0
        index = 0
        for start, end in intervals:
            ans[start] += 1
            ans[end] -= 1
        
        for index in range(maxTime):
            currRooms += ans[index]
            maxRooms = max(currRooms, maxRooms)

        return maxRooms
