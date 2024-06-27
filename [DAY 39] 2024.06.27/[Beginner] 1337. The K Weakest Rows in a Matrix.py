# [103ms] Beats 11.46%
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        max_list, res = [], []
        a=0
        for idx,i in enumerate(mat):
            for j in i:

                if 0 not in i:
                    max_list.append([len(i), idx])
                    break
                elif 1 not in i:
                    max_list.append([0, idx])
                    break
                elif j == 1:
                    a+=1
                elif a != 0:
                    max_list.append([a, idx])
                    a = 0
        max_list.sort()

        for i in range(k):
            res.append(max_list[i][1])
        return res