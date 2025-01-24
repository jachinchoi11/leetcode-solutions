class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        # i think we can do a bfs on this but the directions are that we have to go and reach a terminal node for all the different paths 
        # before we can move on 
        # if we see a terminal node, bascialy the graph[index] = [], then we can say taht path is fine 
        # and then we can essentially add that node into the safe node, as a way to not redo that computation 
        # then that way if anythign points to it can be seen as a safe index, (so we will use a set)
        # the first iteration, we can figure it out for the actual terminal nodes, then we can output it in order 
        # the reason why a bfs might not be as good is to actually seek that cycle 


        res = []
        number_of_nodes = len(graph)
        safe = set()

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
                if dfs(index, set()):
                    res.append(index)
                    safe.add(index)
        return res