class Solution:
    def isPalindrome(self, s: str) -> bool:
        Fo = s.lower()
        Fo = Fo.replace(",", "")
        Fo = Fo.replace("'", "")
        Fo = Fo.replace("?", "")
        Fo = Fo.replace(" ", "")
        Fo = Fo.replace(".", "")
        Fo = Fo.replace(":", "")
        Fo = Fo.replace("!", "")
        new_str = "".join(list(Fo))
        n = len(new_str)
        i, j = 0, n-1
        while i <= j:
            if new_str[i] != new_str[j]:
                return False
            i += 1
            j -= 1
        return True
            
        