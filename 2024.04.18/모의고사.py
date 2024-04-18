# 수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.
# 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
# 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
# 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...
# 1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

def solution(answers):
    answer = []
    answers_num = len(answers)
    
    student_01, student_02, student_03 = [], [], []
    
    score_01, score_02, score_03 = 0, 0, 0
    
    for i in range(answers_num):
        student_01.append((i%5)+1)
        
        if len(student_02) < answers_num:
            if (i%5)+1 != 2:
                student_02.extend([2, (i%5)+1])
            student_02 = student_02[:answers_num]
            
            if i%5 == 0:
                 student_03.extend([(i%5)+3, (i%5)+3])
            elif i%5 < 3:
                student_03.extend([i%5, i%5])
            else :
                student_03.extend([(i%5)+1, (i%5)+1])
            student_03 = student_03[:answers_num]    
    
    for i, ans in enumerate(answers):
        if ans == student_01[i]:
            score_01 += 1
        if ans == student_02[i]:
            score_02 += 1
        if ans == student_03[i]:
            score_03 += 1
    
    if score_01 == max(score_01, score_02, score_03):
        answer.append(1)
    if score_02 == max(score_01, score_02, score_03):
        answer.append(2)
    if score_03 == max(score_01, score_02, score_03):
        answer.append(3)
    
    return answer