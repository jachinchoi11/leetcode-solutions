class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # this is djikstra's problem 
        # we can use a min heap to siolve this problem 
        # but we have to be able to parse through our input 

        edges = defaultdict(list)

        for node, travelNode, time in times:
            edges[node].append((time, travelNode))



        shortest = {}
        minHeap = [(0, k)]

        while minHeap:
            currTime, node = heapq.heappop(minHeap)
            if node in shortest:
                continue
            shortest[node] = currTime

            adj = edges[node]
            
            for t, tN in adj:
                if tN not in shortest:
                    heapq.heappush(minHeap, (currTime + t, tN))

        print(shortest)
        if len(shortest) != n:
            return -1
        return max(list(shortest.values()))