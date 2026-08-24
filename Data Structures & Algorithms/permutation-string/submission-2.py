class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        i = 0
        if len(s2) < k:
            return False
        char_count = [0] * 26
        for char in s1:
            char_count[ord(char) - ord("a")] += 1
        
        while i + k <= len(s2):
            s = s2[i:i+k]
            cnt = [0] * 26
            for char in s:
                cnt[ord(char) - ord("a")] += 1
            if tuple(cnt) == tuple(char_count):
                return True
            i += 1
        return False
            

        