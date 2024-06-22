class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        # 샌드위치 리스트가 비어있지 않으면 while문 실행
        while sandwiches:
		        # 샌드위치의 리스트의 첫번째 요소가 학생 리스트에 있으면
            if sandwiches[0] in students:
		            # 그 요소를 학생 리스트와 샌드위치 리스트에서 삭제
                students.remove(sandwiches[0])
                sandwiches.pop(0)
            # 샌드위치 리스트의 첫번째 요소가 학생리스트에 없으면 while문 정지
            else:
                break
        return len(sandwiches)
