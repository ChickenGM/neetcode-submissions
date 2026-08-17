class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_check = {}
        t_check = {}
        for i in range(len(s)):
            if s[i] not in s_check:
                s_check[s[i]] = 1
            else:
                s_check[s[i]] += 1
        for j in range(len(t)):
            if t[j] not in t_check:
                t_check[t[j]] = 1
            else:
                t_check[t[j]] += 1
        return s_check == t_check