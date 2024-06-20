# [1678ms] Beats 5.02%
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 시간복잡도 O(n log n)
        res = []
        my_list = []

        for n in set(nums):
            my_list.append([nums.count(n), n])

        # 개수 많은 상위 k개
        for i in range(k):
            res.append(sorted(my_list, reverse = True)[i][1])
        return res
