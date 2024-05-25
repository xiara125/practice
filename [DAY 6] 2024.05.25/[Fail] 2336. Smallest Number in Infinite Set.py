class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        stack = []
        alice = -1
        bob = -1

        for num in range(len(nums)//2):
            alice = min(nums)
            nums.remove(min(nums))
            bob = (min(nums))
            nums.remove(min(nums))
            stack.append(bob)
            stack.append(alice)
        return stack