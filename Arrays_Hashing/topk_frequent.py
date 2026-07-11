from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq: dict[int, int] = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        max_freq = max(freq.values())
        bucket: list[list[int]] = [[] for _ in range(max_freq + 1)]
        for num, count in freq.items():
            bucket[count].append(num)

        res: List[int] = []
        for i in range(max_freq, 0, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return res


sol = Solution()
print(sol.topKFrequent([1, 2, 2, 3, 3, 3], 2))
print(sol.topKFrequent([7, 7], 2))
