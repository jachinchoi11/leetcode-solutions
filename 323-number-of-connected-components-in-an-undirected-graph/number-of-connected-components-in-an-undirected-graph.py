class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        connections = defaultdict(list)
        visited = set()

        for i in range(len(edges)):
            pre, after = edges[i]
            connections[pre].append(after)
            connections[after].append(pre)
        
        queue = deque()

        def bfs(queue, connections):
            visited.add(queue[0])
            while queue:
                curr = queue.popleft()
                currList = connections[curr]
                for value in currList:
                    if value not in visited:
                        queue.append(value)
                        visited.add(value)

        
        res = 0
        for node in connections:
            if node not in visited:
                queue.append(node)
                bfs(queue, connections)
                res += 1
        res += n - len(connections)
        return res

