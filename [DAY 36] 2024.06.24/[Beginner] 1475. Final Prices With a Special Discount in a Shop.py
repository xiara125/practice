# [60ms] Beats 7.85%
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        res = []
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                if prices[i] > prices[j] or (i!=j and prices[i] == prices[j]) :
                    res.append(prices[i]-prices[j])
                    break
                elif j == len(prices)-1:
                    res.append(prices[i])
        return res
    



# 추천 풀이

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        for i in range(len(prices)):
            while stack and (prices[stack[-1]] >= prices[i]):
                prices[stack.pop()] -= prices[i]
            stack.append(i)
        return prices