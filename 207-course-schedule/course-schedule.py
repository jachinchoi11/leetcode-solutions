class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # if you can finish all the courses --> essentially, as long as we don't have a cycle
            # as in theres no we havet o have compelteed this to take that 
        
        # essentially, we can start at course 0, and if we ever run into anything again gg 

        path = set() # set to track where you are right now
        visited = set() # set to track cleared courses 
        adj_list = defaultdict(list) # will store from pre req to class 

        for start, end in prerequisites:
            adj_list[end].append(start)
    
        def dfs(curr_course):
            if curr_course in path:
                # this represents the path that we are taking 
                return False
            if curr_course in visited:
                return True
            path.add(curr_course)

            for next_course in adj_list[curr_course]:
                if not dfs(next_course):
                    return False
            path.remove(curr_course) # so must be removed, as we have already dealit with it
            visited.add(curr_course) # using the visited, so that if we go to a course that is checked already, then it should be fine
            return True
        

        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True
        
