# 정수를 저장한 배열, arr 에서 가장 작은 수를 제거한 배열을 리턴하는 함수, solution을 완성해주세요. 단, 리턴하려는 배열이 빈 배열인 경우엔 배열에 -1을 채워 리턴하세요. 예를들어 arr이 [4,3,2,1]인 경우는 [4,3,2]를 리턴 하고, [10]면 [-1]을 리턴 합니다.

def solution(arr):
    answer = []
    least = arr[0]
    least_idx = 0
    
    if len(arr) == 1:
        answer.append(-1)
    else :
        for i in range(len(arr)) :
            if arr[i] < least :
                least = arr[i]
                least_idx = i
        del arr[least_idx]
        answer = arr
    return answer