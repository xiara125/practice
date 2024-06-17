# [226ms] Beats 78.71%
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        res = 0
        for a,b,c in items:
            if ruleKey == "type":
                if a == ruleValue:
                    res += 1
            elif ruleKey == "color":
                if b == ruleValue:
                    res += 1
            else:
                if c == ruleValue:
                    res += 1
        return res