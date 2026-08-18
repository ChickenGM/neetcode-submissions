class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        i, j = 0, n-1
        res = [1] * 2
        while i <= j:
            if numbers[i] + numbers[j] == target:
                res[0] = i+1
                res[1] = j+1
                break
            elif numbers[i] + numbers[j] < target:
                i += 1
            else:
                j -= 1
        return res
        

        