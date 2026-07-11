from typing import List


class Solution:
    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        result: list[str] = []
        i: int = 0
        while i < len(s):
            j = s.find("#", i)
            length = int(s[i:j])
            result.append(s[j + 1 : j + 1 + length])
            i = j + length + 1
        return result


sol = Solution()
s = sol.encode(["Hi", "How", "are", "you", "miamor"])
print(s)
print(sol.decode(s))
