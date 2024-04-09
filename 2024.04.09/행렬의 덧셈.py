def solution(arr1, arr2):
    result = []
    # arr1의 길이만큼 반복
    for i in range(len(arr1)):
		    # arr1의 n번째 수와 arr2의 n번째 수를 합함
		    # 이런 식으로 -> (arr1[i], arr2[i])...
        for a, b in zip(arr1, arr2):
            sum = []
            # 
            for i, j in zip(a, b):
                sum.append(i + j)
            result.append(sum)
        return result