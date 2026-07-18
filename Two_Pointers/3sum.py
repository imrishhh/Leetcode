from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        print(
            "i\tleft\tright\ttarget\tnums[i]\tnums[left]\tnums[right]\tcurrent_sum\tres"
        )
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1
            target = -nums[i]
            if left < right:
                print(
                    "-----------------------------------------------------------------------------------------------------------------"
                )
            while left < right:
                current_sum = nums[left] + nums[right]
                print(
                    f"{i}\t{left}\t{right}\t{target}\t{nums[i]}\t{nums[left]}\t\t{nums[right]}\t\t{current_sum}\t\t{res}\n"
                )
                if current_sum == target:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    print(
                        f"{i}\t{left}\t{right}\t{target}\t{nums[i]}\t{nums[left]}\t\t{nums[right]}\t\t{current_sum}\t\t{res}\n"
                    )
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                        print(
                            f"{i}\t{left}\t{right}\t{target}\t{nums[i]}\t{nums[left]}\t\t{nums[right]}\t\t{current_sum}\t\t{res}\n"
                        )
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                        print(
                            f"{i}\t{left}\t{right}\t{target}\t{nums[i]}\t{nums[left]}\t\t{nums[right]}\t\t{current_sum}\t\t{res}\n"
                        )
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1
                print(
                    f"{i}\t{left}\t{right}\t{target}\t{nums[i]}\t{nums[left]}\t\t{nums[right]}\t\t{current_sum}\t\t{res}\n"
                )
        return res


nums = [-1, 0, 1, 2, -1, -4]
sol = Solution()
sol.threeSum(nums)
