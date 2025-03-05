class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        # we want to minimze the amount of conference rooms, thinking of this just lgoically
        # you want to kind of cram everyone in as much as possible, as in if you use a room,
        # you want it to always be fileld
        # in an ideal world, the intervals are not overlapping, as then you would onlu need one
        # so try to fit it into one room, but add rooms, as you have to go if the prior ones you've already booked
        # are being used

        # so i'm thinking maybe we can potentially create a queue of some sort, where we could pop off 
        # after checking if the end time is bigger than the current time 
        # but that might not be it, cuause it is not sorting necessarily

        # maybe we can use a heap that priorizies the end times? 
            # so we would go through and have a start time, and before we add, pop off anything in there 
            # if start time > time on the heap
            # then we would go on and do that 
            # i believe this sol would work, but it would be O (nlogn) solution
        
        pq = []
        max_rooms = 0
        intervals.sort() # sort it by start times

        for start, end in intervals:
            while pq and pq[0] <= start:
                heapq.heappop(pq)
            
            heapq.heappush(pq, end)

            max_rooms = max(max_rooms, len(pq))
        
        return max_rooms
        





        

