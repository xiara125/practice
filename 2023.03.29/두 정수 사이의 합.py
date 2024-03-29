def solution(a,b):
    answer = 0

    # mim(x,y,z) 매개변수 중 가장 작은 것 선택 
    min_num = min(a,b)
    # max(x,y,z) 매개변수 중 가장 큰 것 선택
    max_num = max(a,b)

    for i in range(min_num, max_num+1):
        answer += i

    return answer