# [32ms]Beats 83.72% of users with Python3
class Solution:
    def fib(self, n: int) -> int:
        fibonacci_list = [0,1]
        if n == 0:
            return 0
        for i in range(2, n):
            fibonacci_list.append(fibonacci_list[i-2]+fibonacci_list[i-1])
        return fibonacci_list[n-1]+fibonacci_list[n-2]