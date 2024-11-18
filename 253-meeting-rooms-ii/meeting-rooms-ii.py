class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # sorted nlogn

        startTime = [] 
        endTime = []
        currRooms, maxRooms = 0, 0
        startP, endP = 0,0

        for start, end in intervals:
            startTime.append(start)
            endTime.append(end)
        
        startTime.sort()
        endTime.sort()

        while startP < len(startTime) and endP < len(endTime):

            if startTime[startP] < endTime[endP]:
                currRooms += 1
                startP += 1
            else:
                currRooms -= 1
                endP += 1
            maxRooms = max(maxRooms, currRooms)

        return maxRooms
