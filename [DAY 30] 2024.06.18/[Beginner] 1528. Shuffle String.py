# [60ms] Beats 18.75%
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = ''
        my_list = list(zip(indices, s))
        for a, b in sorted(my_list):
            res += b
        return res