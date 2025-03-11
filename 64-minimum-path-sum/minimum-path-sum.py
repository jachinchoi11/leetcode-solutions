class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        # we want to minimize the sum it takes to go somewhere
            # however, the weights are not necessarily the same 

            # we could do a bfs of all the possivbiltiies, but i think it would be better to use a priority queeu
                # that prioiritizes the smallest sum, and then put all its neighbors in it 
            
            # we could have a visited set for each apporach no that doesn't make sense

        pq = []
                   
        displacement = [[0, 1], [1, 0]]

        heapq.heappush(pq, (grid[0][0], 0, 0)) # will put in the sum, row, col 

        shortest_dist = {(0, 0): grid[0][0]}

        while pq:
            curr_sum, curr_row, curr_col = heapq.heappop(pq)

            if curr_row == len(grid) - 1 and curr_col == len(grid[0]) - 1:
                return curr_sum
            
            for dr, dc in displacement:
                new_row = dr + curr_row
                new_col = dc + curr_col
                if new_row < 0 or new_col < 0 or new_row == len(grid) or new_col == len(grid[0]):
                    continue
            
                if (new_row, new_col) not in shortest_dist:
                    heapq.heappush(pq, (curr_sum + grid[new_row][new_col], new_row, new_col))
                    shortest_dist[(new_row, new_col)] = curr_sum + grid[new_row][new_col]
        
        return -1