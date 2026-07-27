class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums_set = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in nums_set:
                length = 1
                while num + length in nums_set:
                    length += 1
                longest = max(longest, length)
        return longest


nums = [20, 4, 7, 8, 9, 10, 1, 2, 30]
sol = Solution()
print(sol.longestConsecutive(nums))
