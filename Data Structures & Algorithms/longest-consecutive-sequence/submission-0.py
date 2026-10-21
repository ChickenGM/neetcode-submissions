class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_check = set(nums)
        ans = 0
        for num in nums_check:
            if num - 1 not in nums_check:
                current_streak = 1
                curr = num
                while curr + 1 in nums_check:
                    curr += 1
                    current_streak += 1
                ans = max(ans, current_streak)
        return ans
        