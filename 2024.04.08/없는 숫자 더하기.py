def solution(numbers):
    answer = 0

    for i in set(range(10)) ^ set(numbers):
        answer += i
    
    return answer