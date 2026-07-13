from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        res: List[int] = [1] * length
        for i in range(1, length):
            res[i] = res[i - 1] * nums[i - 1]
        backtracker = 1
        for i in range(length - 1, -1, -1):
            res[i] *= backtracker
            backtracker *= nums[i]
        return res


sol = Solution()
print(sol.productExceptSelf([1, 2, 3, 4]))
print(sol.productExceptSelf([1, 0, 3, 5]))
