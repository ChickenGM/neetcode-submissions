class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_s = list(s)
        char_t = list(t)
        char_s.sort()
        char_t.sort()
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if char_s[i] != char_t[i]:
                return False
        return True