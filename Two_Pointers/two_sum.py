from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        while i < j:
            current_sum = numbers[i] + numbers[j]
            if current_sum == target:
                return [i + 1, j + 1]
            if current_sum < target:
                i += 1
            else:
                j -= 1
        return []


nums = [1, 2, 3, 4]
target = 4
sol = Solution()
print(sol.twoSum(nums, target))
