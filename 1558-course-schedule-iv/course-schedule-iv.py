class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        # first we can set up the adj list taht will keep track of the prerequisites and map them to their children
        # in the query, we can just go ahead and dfs and bfs and see if we're abel to see the second element or we hit a cycle and then it would be wrong 
        adj = defaultdict(list)

        for start_node, end_node in prerequisites:
            adj[start_node].append(end_node)
        
        visited = set()

        '''def dfs(curr_node, ending_node):

            if curr_node == ending_node:
                return True
            
            visited.add(curr_node)

            for i in adj[curr_node]:
                if dfs(i, ending_node):
                    return True
            
            visited.remove(curr_node)
            return False
            the dfs approach is too slow in this case, so maybe we can look at the bfs case 

            '''
        
        def bfs(curr_node, visited):
            queue.append(curr_node)
            while queue:
                curr_val = queue.popleft()
                visited.add(curr_val)
                if curr_node != curr_val:
                    reachable[curr_node].add(curr_val)
                
                for new_node in adj[curr_val]:
                    if new_node not in visited:
                        queue.append(new_node)
        
        # wait during this bfs i think we should add all the answers for this one 
        queue = deque()
        reachable = defaultdict(set)
        res = [False] * len(queries)

        for i in range(numCourses):
            bfs(i, set())
        for index, (startQ, endQ) in enumerate(queries):
            if endQ in reachable[startQ]:
                res[index] = True
        return res
