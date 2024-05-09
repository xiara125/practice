def solution(babbling):
    answer = 0
            
    for i in range(len(babbling)):
        babbling[i] = babbling[i].replace('aya', "1")
        babbling[i] = babbling[i].replace('ye', "2")
        babbling[i] = babbling[i].replace('woo', "3")
        babbling[i] = babbling[i].replace('ma', "4")
    
    for i, babb in enumerate(babbling):
        for j in range(1, len(babb)):
            if babb[j] == babb[j-1]:
                babbling[i] += 'abc'
    
    for ba in babbling:
        if ba.isdigit():
            answer += 1
    
    return answer