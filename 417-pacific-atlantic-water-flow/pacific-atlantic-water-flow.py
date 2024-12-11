class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        # brute force would be to just bfs and see if theres a path to lat least the up and left edge/ right and dwon edge 
        # two booleans to track it

        rows, cols = len(heights), len(heights[0])
        adj = [[0,1], [1,0], [-1, 0], [0,-1]]
        pacificQueue = deque()
        atlanticQueue = deque()

        pacific = set()
        atlantic = set()
        res = []

        for row in range(rows):
            pacificQueue.append((row, 0))
            atlanticQueue.append((row, cols - 1))
            pacific.add((row, 0))
            atlantic.add((row, cols - 1))
        
        for col in range(cols):
            pacificQueue.append((0, col))
            atlanticQueue.append((rows - 1, col))
            pacific.add((0, col))
            atlantic.add((rows - 1, col))

        
        while pacificQueue:
            currX, currY = pacificQueue.popleft()
            for dr, dc in adj:
                newX = currX + dr
                newY = currY + dc
                if newX < 0 or newY < 0 or newX == rows or newY == cols or heights[newX][newY] < heights[currX][currY] or (newX, newY) in pacific:
                    continue
                pacificQueue.append((newX, newY))
                pacific.add((newX, newY))
        
        while atlanticQueue:
            currR, currC = atlanticQueue.popleft()

            for dr, dc in adj:
                newR = currR + dr
                newC = currC + dc

                if newR < 0 or newC < 0 or newR == rows or newC == cols or heights[newR][newC] < heights[currR][currC] or (newR, newC) in atlantic:
                    continue
                atlanticQueue.append((newR, newC))
                atlantic.add((newR, newC))

        for currR, currC in pacific:
            if (currR, currC) in atlantic:
                res.append([currR, currC])
        
        return res
        


