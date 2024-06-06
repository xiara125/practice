# # 오버타임

# class Solution:
#     def countBits(self, n: int) -> List[int]:
#         second = 0
#         answer = []
#         if not n:
#             return [0]
#         for num in range(n+1):
#             for i in range(num, -1, -1):
#                 if num//(2**i) > 0:
#                     second += 1
#                     num -= 2**i
#             answer.append(second)
#             second = 0

#         return answer


class Solution:
    def countBits(self, n: int) -> List[int]:
        answer = [0]
        for num in range(1, n+1):
            answer.append(sum(map(int,bin(num)[2:])))

        return answer