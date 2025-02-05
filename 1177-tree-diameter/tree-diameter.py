class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        # the logic for this problem is to find the farthest node from 0 and then from that point on, find the farthest node from there 
        hashset = set()
        adj_list = defaultdict(list)

        for start, end in edges:
            adj_list[start].append(end)
            adj_list[end].append(start)

            hashset.add(start)
            hashset.add(end)
        
        queue = deque()
        def bfs(node, visited):
            last_node = node
            queue.append((node, 0))
            curr_max_diameter = 0
            visited.add(node)
            while queue:
                for _ in range(len(queue)):
                    curr_node, curr_diameter = queue.popleft()
                    for other_node in adj_list[curr_node]:
                        if other_node not in visited:
                            queue.append((other_node, curr_diameter + 1))
                            visited.add(other_node)
                    last_node = curr_node
                    curr_max_diameter = max(curr_max_diameter, curr_diameter)
            return last_node, curr_max_diameter

        next_node, _ = bfs(0, set())
        _, ans = bfs(next_node, set())
    
        return ans