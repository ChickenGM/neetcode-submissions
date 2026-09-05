class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_val = max(piles)
        if len(piles) == h:
            return max_val
        low, high = 1, max_val
        k, ans = 0, max_val
        while low <= high:
            mid = (high - low) // 2 + low
            k = mid
            t = 0
            for pile in piles:
                if pile % k == 0:
                    t += (pile // k)
                else:
                    t += (pile // k) + 1
            if t <= h:
                ans = k
                high = mid - 1
            elif t > h:
                low = mid + 1
        return ans

            

        
        