class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) != n - 1:
            return False
        
        adj = defaultdict(list)

        for start, end in edges:
            adj[start].append(end)
            adj[end].append(start)
        
        visited = set()

        def dfs(node):
            if node in visited:
                return False
            visited.add(node)
            for adjC in adj[node]:
                dfs(adjC)
            return True

        return True if dfs(0) and len(visited) == n else False

