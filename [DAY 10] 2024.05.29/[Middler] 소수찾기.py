def solution(brown, yellow):
    answer = []
    for i in range(yellow,0,-1):
        if yellow%i == 0 and (i*2)+((yellow//i)*2)+4 == brown and i>=(yellow//i):
            answer.append(i+2)
            answer.append((yellow//i)+2)
    return answer