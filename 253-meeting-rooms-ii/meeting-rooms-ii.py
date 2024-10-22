class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        start = []
        end = []
        for i in range(len(intervals)):
            start.append(intervals[i][0])
            end.append(intervals[i][1])
        start = sorted(start)
        end = sorted(end)


        s, e = 0,0
        currRooms, maxRooms = 0, 0


        while s < len(start) and e < len(end):
            if start[s] < end[e]:
                currRooms += 1
                s += 1
            else:
                # becasue when its tied we have to - first
                e += 1
                currRooms -= 1
            print(maxRooms)
            maxRooms = max(currRooms, maxRooms)
    
        return maxRooms

            

        
            
                
         