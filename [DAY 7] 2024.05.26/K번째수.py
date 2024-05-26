def solution(array, commands):
    answer = []
    arr = []
    for com in commands:
        # array를 범위만큼 잘라 arr에 저장
        arr = array[com[0]-1:com[1]]
        # answer리스트에 추가
        answer.append(sorted(arr)[com[2]-1])
    return answer