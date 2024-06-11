# [55ms]Beats 18.81% of users with Python3
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        answer = 0
        if nums[-1] < target:
            return len(nums)
        for i, num in enumerate(nums):
            print(i)
            if nums[i] == target :
                print("nums= ", nums[i])
                return i
            elif nums[i] > target:
                print(i)
                return i