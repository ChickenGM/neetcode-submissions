class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fre_map = defaultdict(int)
        for num in nums:
            if num in fre_map:
                fre_map[num] += 1
            else:
                fre_map[num] = 1
        ans = []
        for num, cnt in fre_map.items():
            ans.append([cnt, num])
        ans.sort()
        res = []
        while len(res) < k:
            res.append(ans.pop()[1])
        return res
            


        


        
        