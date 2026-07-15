class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        i, j = 0, n - 1
        small = s.lower()
        while i < j:
            if not small[i].isalnum():
                i += 1
                continue
            if not small[j].isalnum():
                j -= 1
                continue
            if small[i] != small[j]:
                return False
            i += 1
            j -= 1
        return True


s = "Was it a car or a cat I saw?"
s2 = "tab a cat"
sol = Solution()
print(sol.isPalindrome(s))
print(sol.isPalindrome(s2))
