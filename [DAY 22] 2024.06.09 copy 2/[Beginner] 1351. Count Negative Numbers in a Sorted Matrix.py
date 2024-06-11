# [98ms] Beats 82.15% of users with Python3
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        answer = 0
        for gri in grid:
            for g in gri:
                if g < 0:
                    answer += 1
        return answer
    

# 도움을 받아 풍 풀이
# [102 ms] Beats 60.47% of users with Python3
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0]) if rows > 0 else 0
        
        count = 0
        row = 0
        col = cols - 1
        
        while row < rows and col >= 0:
            if grid[row][col] < 0:
                count += (rows - row)  # 현재 행부터 끝까지의 음수 개수 추가
                col -= 1  # 다음 열로 이동
            else:
                row += 1  # 다음 행으로 이동
        
        return count