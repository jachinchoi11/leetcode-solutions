class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        res = []
        number_of_nodes = len(graph)
        safe = set()
        visited = set()
        
        def dfs(index, visited):
            if index in safe or graph[index] == []:
                return True
            if index in visited:
                return False
            visited.add(index)
            for neighbors in graph[index]:
                if not dfs(neighbors, visited):
                    return False
            visited.remove(index)
            safe.add(index)
            return True

        for index in range(number_of_nodes):
            if graph[index] == [] or index in safe:
                res.append(index)
            else:
                if dfs(index, visited):
                    res.append(index)
        return res