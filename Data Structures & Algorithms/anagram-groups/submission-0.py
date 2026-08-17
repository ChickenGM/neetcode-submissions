class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            x = list(word)
            x.sort()
            x = str(x)
            if x in groups:
                groups[x].append(word)
            else:
                groups[x] = []
                groups[x].append(word)
        res = []
        for anagrams in groups:
            res.append(groups[anagrams])
        return res

        