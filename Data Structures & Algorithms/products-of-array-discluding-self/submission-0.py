class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre, sur = 1, 1
        pre_list = [1] * n
        sur_list = [1] * n 
        res = [0] * n
        for i in range(n-1):
            pre *= nums[i]
            pre_list[i+1] = pre
            sur *= nums[n-1-i]
            sur_list[n-2-i] = sur
        for j in range(n):
            res[j] = pre_list[j] * sur_list[j]
        return res

        

        

        