# [291ms] Beats 84.52%
class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
				    # nums의 길이가 3보다 짧으면 -1을 리턴하고
				    # 오른차순 정렬된 nums의 길이가 3보다 길면 nums의 잎어서 2번째 숫자 리턴
            return -1 if len(nums) < 3 else sorted(nums)[1]