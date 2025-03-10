class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:


        indegree = [0] * numCourses
        adj_list = defaultdict(list)
        courses_done = 0

        for course, prereq in prerequisites:
            adj_list[prereq].append(course) # prereq --> course
            indegree[course] += 1
        
        queue = deque([i for i in range(len(indegree)) if indegree[i] == 0])

        while queue:
            curr_course = queue.popleft()
            courses_done += 1
            for other_course in adj_list[curr_course]:
                # here, if we have processed it already, that means that there is less than one prereq
                indegree[other_course] -= 1
                if indegree[other_course] == 0:
                    # whenever it has no prereqs left that is when we should take it out
                    queue.append(other_course)
        
        return courses_done == numCourses

