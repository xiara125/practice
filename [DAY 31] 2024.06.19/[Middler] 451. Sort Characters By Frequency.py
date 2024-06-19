# [60ms] Beats 20.22%
class Solution:
    def frequencySort(self, s: str) -> str:
        res = ""
        my_dict = {}
        string = set(s)

        for i in string:
            my_dict[i] = s.count(i)

        my_dict = sorted(my_dict.items(), key= lambda item:item[1], reverse=True)

        for k,v in my_dict:
            res += (k*v)

        return res