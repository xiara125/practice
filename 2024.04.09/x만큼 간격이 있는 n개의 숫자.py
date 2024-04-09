def solution(x, n):
    answer = []
    
    # 1부터 n+1까지 반복
    for i in range(1, n+1):
		    # x를 i만큼 곱한 수를 answer에 추가
        answer.append(x*i)
    
    return answer