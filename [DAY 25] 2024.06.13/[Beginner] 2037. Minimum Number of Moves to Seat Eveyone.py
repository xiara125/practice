# [64ms] Beats 27.12%
class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        new_seats = sorted(seats)
        new_students = sorted(students)
        answer = 0

        for i in range(len(seats)):
            answer += max(new_seats[i], new_students[i]) - min(new_seats[i], new_students[i])
        return answer