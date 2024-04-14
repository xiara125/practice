# 자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return 하는 solution 함수를 만들어 주세요.
# 예를들어 N = 123이면 1 + 2 + 3 = 6을 return 하면 됩니다.

def solution(n):
    answer = 0
    n_list = []
    
    for i in str(n):
        n_list.append(i)
        
    for i in n_list:
        answer += int(i)
        
    return answer