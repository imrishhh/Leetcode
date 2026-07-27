class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        if len(nums) < 2:
            return []
        complement_map: dict[int, int] = {}
        for i, num in enumerate(nums):
            diff = target - num[i]
            if diff in complement_map:
                return [complement_map[diff], i]
            complement_map[num] = i
        return []


sol = Solution()
print(sol.twoSum([1, 2, 3, 4, 5, 6, 8, 9], 10))
