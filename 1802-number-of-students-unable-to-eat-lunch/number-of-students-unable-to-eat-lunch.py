class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        sandwiches = deque(sandwiches)
        students = deque(students)
        count = 0
        while students:
            if sandwiches[0] != students[0]:
                s = students.popleft()
                students.append(s)
                count += 1
            else:
                sandwiches.popleft()
                students.popleft()
                count = 0
            if count == len(students):
                break
        return len(students)