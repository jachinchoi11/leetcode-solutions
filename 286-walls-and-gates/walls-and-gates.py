class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        # we can do a bfs here 
        # first go through it and find all the empty room allocations 
        # and then we run a bfs and breka whenever we see a gate 
        # name that specific one 
        rows, cols = len(rooms), len(rooms[0])

        queue = deque()
        adj = [[0,1], [1,0], [-1,0], [0,-1]]

        for row in range(rows):
            # find all the gates
            for col in range(cols):
                if rooms[row][col] == 0:
                    queue.append((row, col))
        
        while queue:
            for _ in range(len(queue)):
                currRow, currCol = queue.popleft()
                for dr, dc in adj:
                    newRow, newCol = currRow + dr, currCol + dc
                    if newRow < 0 or newRow == rows or newCol < 0 or newCol == cols or rooms[newRow][newCol] != 2**31 - 1:
                        continue
                    rooms[newRow][newCol] = rooms[currRow][currCol] + 1
                    queue.append((newRow, newCol))


        
        

                       
        