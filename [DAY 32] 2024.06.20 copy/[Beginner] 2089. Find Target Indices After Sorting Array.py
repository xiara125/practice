# 나의풀이 1
# [79ms] Beats 5.07%
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        res = []
        for i in range(len(nums)):
		        # 반복할때마다 정렬된 리스트를 새로 만듦(상대적으로 낮은 효율성)
            if sorted(nums)[i] == target:
                res.append(i)
        return res
    
# 나의풀이 2
# [53ms] Beats 24.23%
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        res = []
        # nums를 직접 정렬하지 않고 새로운 리스트를 생성하는 것(상대적으로 낮은 효율성)
        for i, num in enumerate(sorted(nums)):
            if num == target:
                res.append(i)
        return res
    
# 나의풀이 3
# [48ms] Beats 54.85%
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        res = []
        # 입력받은 리스트 nums 자체를 정렬함으로 새로운 리스트를 만들지 않아도 되기에 상대적으로 효율적인 메모리 사용률을 보임
        nums.sort()
        for i,num in enumerate(nums):
            if num == target:
                res.append(i)
        return res