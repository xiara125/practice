# [38ms] Beats 62.09%
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count_1 = s.count('1')
        res = s.count('0') * '0'

        print(count_1)
        while count_1 != 1:
            res = "1" + res
            count_1 -= 1

        res += '1'

        return res