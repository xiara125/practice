# [44ms] Beats 19.80%
class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        res = ""
        eng = "abcdefghijklmnopqrstuvwxyz"
        new_key = ''

        for k in key:
            if k == " ":
                pass
            elif k not in new_key:
                new_key += k
        print(new_key)
        my_dict = dict(zip(new_key, eng))

        for m in message:
            if m == " ":
                res += " "
            else:
                res += my_dict[m]
        return res