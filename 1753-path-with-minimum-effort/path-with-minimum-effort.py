class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # for we can have a priority queue with the current differrence and the current value

        # when we pop it out the pq, then we can see the previous value, and then do the difference of them and update it 

        # keep on going until we hit the bottom right cell 
        # if it has already been visited, that means there is already a shorter path to that location 

        # djikstra's algorithm, one it hits the bottom right, return the effort level 

        # start with the min and max as current and 0 

        pq = [(0, heights[0][0], 0, 0)]
        rows, cols = len(heights), len(heights[0])
        res = 0
        visit = set()

        while pq:
            currDiff, prevValue, row, col = heapq.heappop(pq)
            directions = [[0, 1], [1, 0], [-1, 0], [0,-1]]
            if row == rows - 1 and col == cols - 1:
                return currDiff
            visit.add((row , col))
            for dr, dc in directions:
                newR = row + dr
                newC = col + dc
                if min(newR, newC) < 0 or newR == rows or newC == cols or (newR, newC) in visit:
                    continue
                newDiff = max(currDiff, abs(heights[newR][newC] - prevValue))
                heapq.heappush(pq, (newDiff, heights[newR][newC], newR, newC))
        
        return -1







