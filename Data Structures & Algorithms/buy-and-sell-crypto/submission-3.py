class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        l = 0
        res = 0
        for r in range(n):
            while prices[r] < prices[l]:
                l += 1
            
            profit = prices[r] - prices[l]
            res = max(profit, res)
        return res


            
        