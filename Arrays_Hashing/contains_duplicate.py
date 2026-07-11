from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        trackerSet: set[int] = set()
        for num in nums:
            if num in trackerSet:
                return True
            trackerSet.add(num)
        return False


print(Solution().hasDuplicate([1, 1, 2, 3, 4, 5]))
print(Solution().hasDuplicate([1, 2, 3, 4, 5]))
print(Solution().hasDuplicate([1, 2, 3, 4, 5, 5]))
