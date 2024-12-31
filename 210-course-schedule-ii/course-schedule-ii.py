class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prevMap = defaultdict(list)

        for start, end in prerequisites:
            prevMap[start].append(end)
        path = set()
        res = []
        visited = set()

        def topological_sort(node):
            if node in path:
                return False
            if node in visited:
                return True
            path.add(node)

            for neighbors in prevMap[node]:
                if topological_sort(neighbors) == False:
                    return False
            
            visited.add(node)
            path.remove(node)
            res.append(node)
            return True
        
        for node in range(numCourses):
            if not topological_sort(node):
                return []
        return res
        
        
