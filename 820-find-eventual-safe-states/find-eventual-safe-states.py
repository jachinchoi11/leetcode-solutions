class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # the more optimal appraochw woudl be to keep track of whether it is safe or not 
        res = []
        number_of_nodes = len(graph)
        safe = {}
        visited = set()
        
        def dfs(index, visited):
            # the reason why is because we assume that it will be False at the beginning
            if index in safe:
                return safe[index]
            safe[index] = False
            if index in visited:
                return False
            visited.add(index)
            for neighbors in graph[index]:
                if not dfs(neighbors, visited):
                    return False
            visited.remove(index)
            safe[index] = True
            return True
    
        for index in range(number_of_nodes):
            if dfs(index, visited):
                res.append(index)
        return res