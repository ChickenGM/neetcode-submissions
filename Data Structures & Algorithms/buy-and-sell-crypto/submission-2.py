class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        res = 0
        for r in range(n-1, -1, -1):
            l = 0
            while l < r:
                res = max(res, prices[r] - prices[l])
                l += 1
        return res


            
        