class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # so since this is already reversed, lets jsut go about it like this 

        # set up the adjacency list 
        # all you have to do in this case, is to see if it is possible to finsih it 
        # if you have a cycle in this case, you will not be abel to finish all the classes 

        path = set()

        adj = defaultdict(list)

        for start, end in prerequisites:
            adj[start].append(end)
        
        for node in range(numCourses):
            if not self.dfs(node, adj, path):
                return False
        return True

    def dfs(self, node, adj, path):
        if node in path:
            return False
        path.add(node)
        if node in adj:
            for neighbor in adj[node]:
                if not self.dfs(neighbor, adj, path):
                    return False
            adj[node] = []
        path.remove(node)
        return True
        



