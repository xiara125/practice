# [88ms] Beats 63.34%
class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:

        for i in range(len(grid)):
            grid[i].sort()

        grid = list(zip(*grid))

        max_values = []
        for row in grid:
            max_value = max(row)
            max_values.append(max_value)

        return sum(max_values)
    
# 힙 사용 예시 01
class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for row in grid:
            heapify(row)

        return sum(max(heappop(row) for row in grid) for _ in range(len(grid[0])))
    
# 힙 사용 예시 02
class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for row in grid:
            heapq.heapify(row)

        res = 0
        while grid[0]:
            tmp = []
            for row in grid:
                tmp.append(heapq.heappop(row))
            res += max(tmp)

        return res