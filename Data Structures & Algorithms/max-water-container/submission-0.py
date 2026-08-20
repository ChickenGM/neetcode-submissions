class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        n = len(heights)
        l, r = 0, n-1
        while l <= r:
            h = min(heights[l], heights[r])
            res = max(res, h * (r - l))
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return res