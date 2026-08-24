class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        result = 0
        check = set()
        n = len(s)
        for r in range(n):
            while s[r] in check:
                check.remove(s[l])
                l += 1

            check.add(s[r])
            window = (r - l) + 1
            result = max(result, window)
        return result
        