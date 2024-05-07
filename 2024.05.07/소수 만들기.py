def solution(nums):
    answer = 0

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                total = nums[i]+nums[j]+nums[k]
    
                for x in range(2, total) :
                    if total%x == 0:
                        break
                    if x == total-1:
                        answer+=1

    return answer