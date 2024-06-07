class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        answer = []
        m_li = []

        for i in range(1, numRows+1):
            for j in range(1, i+1):
                if i==1 or j==1 or j==i:
                    m_li.append(1)
                else:
                    m_li.append((answer[i-2][j-2])+((answer)[i-2][j-1]))
            answer.append(m_li)
            m_li = []
        return answer