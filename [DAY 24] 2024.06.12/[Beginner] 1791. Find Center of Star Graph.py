# [643ms] Beats 88.05% of users with Python3
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        answer = list(set(edges[0]) & set(edges[1]))
        return answer[0]