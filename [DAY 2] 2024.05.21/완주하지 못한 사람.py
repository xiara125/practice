def solution(participant, completion):

    myList = list(zip(sorted(participant), sorted(completion)))
    for i in myList:
        if i[0] != i[1]:
            return i[0]
            break
    return sorted(participant)[-1]