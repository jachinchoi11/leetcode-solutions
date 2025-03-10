class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # so we need to find a way to get the ordering of this problem correct, however, i thought about it and there can be several orderings 

        # for example: we have 0 --> 1 --> 2 --> 3
            # so techncially 1 and 2 could be swapped, as long they follow the coposite ordering
        
        # we coudl use the bfs (kahns approach to this)

        # so we need to start with the least prereqs to the most prereqs 
            # i think we can use kahns alogirthm here
        res = []
        indegree = [0] * numCourses
        adj_list = defaultdict(list)

        for course, prereq in prerequisites:
            adj_list[prereq].append(course)
            indegree[course] += 1

        queue = deque([course for course in range(len(indegree)) if indegree[course] == 0]) # will get our values to where if the course has no prereqs that will be first 


        while queue:
            curr_course = queue.popleft()
            res.append(curr_course)

            for next_course in adj_list[curr_course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    queue.append(next_course)
        
        return res if len(res) == numCourses else []




        
