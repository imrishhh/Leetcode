class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagramMap: dict[tuple[int, ...], list[str]] = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            key = tuple(count)
            if key not in anagramMap:
                anagramMap[key] = []
            anagramMap[key].append(s)
        return list(anagramMap.values())


sol = Solution()
print(
    sol.groupAnagrams(["hat", "cat", "bat", "tab", "tac", "lick", "kicl", "mim", "imm"])
)
