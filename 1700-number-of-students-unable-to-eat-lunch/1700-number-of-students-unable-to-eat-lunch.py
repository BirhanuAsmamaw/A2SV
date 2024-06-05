class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        from collections import deque
        
        students = deque(students)
        sandwiches = deque(sandwiches)
        
        count = 0
        while students:
            if students[0] == sandwiches[0]:
                students.popleft()
                sandwiches.popleft()
                count = 0
            else:
                students.append(students.popleft())
                count += 1
            
            if count == len(students):
                break
        
        return len(students)