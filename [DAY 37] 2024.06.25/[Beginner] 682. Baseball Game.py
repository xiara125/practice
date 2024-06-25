# [45ms] Beats 50.31%
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = 0
        my_list = []

        for i, op in enumerate(operations):
            if op == "+":
                my_list.append(my_list[-1]+my_list[-2])
            elif op == "D":
                my_list.append(my_list[-1]*2)
            elif op == "C":
                my_list.pop()
            else:
                my_list.append(int(op))
        return sum(my_list)

