from collections import deque
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        queue = deque(students)
        sandwiches_index = 0
        skipped = 0

        while queue:
            # if student and sandwich matches
            if queue[0] == sandwiches[sandwiches_index]:
                queue.popleft()
                sandwiches_index += 1
                skipped = 0
            else:
                currentStudent = queue.popleft()
                queue.append(currentStudent)
                skipped += 1

                if skipped == len(queue):
                    break
                
        return len(queue)


        