class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        
        # Pattern: Add into the minHeap incrementally when a task becomes available 
        # Be Greedy about it (end times in this case)
        
        minHeap = []
        maximum_events = 0 
        maximum_time = max(event[1] for event in events)
        events_pointer = 0
        events.sort()

        for current_time in range(1, maximum_time + 1):
            # during each iteartion of time, we will insert the start
            # you only add to the minHeap, when soemthing is actually available
            # that is why we can just prioritize the endTimes 
            while events_pointer < len(events) and events[events_pointer][0] == current_time:
                heapq.heappush(minHeap, events[events_pointer][1])
                events_pointer += 1
            
            while minHeap and minHeap[0] < current_time:
                heapq.heappop(minHeap)
            
            if minHeap:
                heapq.heappop(minHeap)
                maximum_events += 1
            
        return maximum_events