class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        res = [0, 0]
        visited = {}
        for i in range(n):
            x = target - nums[i]
            if x not in visited:
                visited[nums[i]] = i
            else:
                res[0] = visited[x]
                res[1] = i
        return res




        