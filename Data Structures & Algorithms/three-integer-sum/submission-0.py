class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        ans_check = set()
        for i in range(n-2):
            find_x = -nums[i]
            j, k = i+1, n-1
            while j < k:
                if nums[j] + nums[k] == find_x and (nums[i], nums[j], nums[k]) not in ans_check:
                    temp = [nums[i], nums[j], nums[k]]
                    ans_check.add((nums[i], nums[j], nums[k]))
                    res.append(temp)
                    j += 1
                    k -= 1
                elif nums[j] + nums[k] < find_x:
                    j += 1
                else:
                    k -= 1
        return res
                
        