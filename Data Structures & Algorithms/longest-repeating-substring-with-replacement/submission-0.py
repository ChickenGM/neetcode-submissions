class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        n = len(s)
        l = 0
        check = {}
        for r in range(n):
            if s[r] in check:
                check[s[r]] += 1
            else:
                check[s[r]] = 1
            best_fre = max(check.values())
            max_len = (r - l) + 1
            while best_fre + k < max_len:
                check[s[l]] -= 1
                l += 1
                max_len = (r - l) + 1
            res = max(res, max_len)
        return res
                

        