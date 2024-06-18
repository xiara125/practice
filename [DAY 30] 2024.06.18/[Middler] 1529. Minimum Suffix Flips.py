# [62ms] Beats 41.73%
class Solution:
    def minFlips(self, target: str) -> int:
        res = 1

        if target[0] == "0":
            res -= 1

        for i in range(1, len(target)):
            if target[i] != target[i-1]:
                res += 1

        return res